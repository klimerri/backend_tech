Запуск виртуального окружения
venv\Scripts\activate

Установка пакетов
pip install -r requirements.txt

Запуск сервера 
python -m uvicorn src.main:app --reload
Запустится на http://127.0.0.1:8000

В файле src/database.py необходимо заменить строчку с подключением: 
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:3745@localhost:3306/backend_engineer"

Настройка БД через MySQL Workbench:
Открыть Workbench 
Запустить локальный сервер
Server -> Data Import -> Import from Self-Contained File -> выбрать файл src/db/Dump20260511.sql -> Start import 