from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from src.models import Task, Engineer, TaskType, Skill, EngineeringSkill, Request


def plan_new_tasks(db: Session):
    """
    Планирование новых заявок согласно алгоритму.
    """
    # 1. Получить список новых заявок
    new_tasks = db.query(Task).filter(Task.status == 'new').all()

    if not new_tasks:
        return []

    # 3. Упорядочить заявки: по приоритету, затем по времени создания обращения
    new_tasks.sort(key=lambda t: (t.priority, t.request.date))

    assigned_tasks = []

    for task in new_tasks:
        # 4.1. Определить требования заявки
        task_type = task.task_type
        required_skills = task_type.skills
        duration_by_grade = {
            'junior': task_type.junior_time,
            'middle': task_type.middle_time,
            'senior': task_type.senior_time
        }

        # 4.2. Сформировать множество кандидатов
        candidates = db.query(Engineer).filter(
            Engineer.id_location == task.id_location,
            Engineer.workload < Engineer.weekly_hours
        ).all()

        # Фильтр по компетенциям
        candidates = [e for e in candidates if all(
            any(es.id_skill == s.id for es in e.engineering_skills) for s in required_skills
        )]

        # 4.3. Отсортировать кандидатов
        def competence(e):
            return sum(es.level for es in e.engineering_skills if any(s.id == es.id_skill for s in required_skills))

        candidates.sort(key=lambda e: (e.workload, -competence(e)))

        # 4.4. Проверка инженеров
        for engineer in candidates:
            grade = engineer.seniority
            duration = duration_by_grade[grade]


            # Определить ближайший рабочий день для старта
            created_dt = task.created_at
            now = datetime.now()
            start_date = max(created_dt.date(), now.date())
            # Если сегодня/стартовый день выходной, сдвигаем на следующий рабочий день
            while start_date.weekday() > 4:
                start_date += timedelta(days=1)

            # Если сегодня и сейчас уже после 19:00, сдвигаем на следующий рабочий день
            if start_date == now.date() and now.hour >= 19:
                start_date += timedelta(days=1)
                while start_date.weekday() > 4:
                    start_date += timedelta(days=1)

            start_week_dt = datetime.combine(start_date, datetime.min.time())

            # Найти свободный интервал
            slot = find_free_slot(db, engineer, duration, start_week_dt)
            if slot:
                start_time, end_time = slot
                # 4.5. Фиксация назначения
                task.id_engineer = engineer.id
                task.start_time = start_time
                task.completion_time = end_time
                task.status = 'process'
                engineer.workload += duration
                db.commit()
                assigned_tasks.append(task)
                break

    return assigned_tasks


def find_free_slot(db: Session, engineer: Engineer, duration: int, start_week: datetime):
    """
    Найти ближайший свободный непрерывный интервал в рабочей неделе.
    Рабочая неделя: понедельник-пятница, 10:00-19:00.
    """
    # Существующие назначения
    existing_tasks = db.query(Task).filter(
        Task.id_engineer == engineer.id,
        Task.status == 'process',
        Task.start_time >= start_week,
        Task.start_time < start_week + timedelta(days=7)
    ).all()
    intervals = [(t.start_time, t.completion_time) for t in existing_tasks]

    # Начать с понедельника 10:00
    current = start_week + timedelta(hours=10)
    end_week = start_week + timedelta(days=5, hours=19)  # Пятница 19:00

    while current + timedelta(hours=duration) <= end_week:
        proposed_end = current + timedelta(hours=duration)

        # Проверить рабочие часы
        day = current.weekday()
        if day > 4:  # Выходные
            current = start_week + timedelta(days=7, hours=10)  # Следующий понедельник
            continue

        if proposed_end.date() != current.date():  # Переход на следующий день
            current += timedelta(hours=1)
            continue

        if current.hour < 10 or proposed_end.hour > 19 or (day == 4 and proposed_end.hour > 19):
            current += timedelta(hours=1)
            continue

        # Проверить пересечения
        overlapping = [(start, end) for start, end in intervals if start < proposed_end and end > current]
        if not overlapping and engineer.workload + duration <= engineer.weekly_hours:
            return current, proposed_end

        if overlapping:
            # Сдвинуть current на конец ближайшего пересекающегося интервала
            current = max(end for start, end in overlapping)
            # Перейти к следующему часу, если вдруг попали не на целый час
            if current.minute != 0 or current.second != 0 or current.microsecond != 0:
                current = current.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
        else:
            current += timedelta(hours=1)

    return None