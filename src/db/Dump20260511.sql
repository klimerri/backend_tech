-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: backend_engineer
-- ------------------------------------------------------
-- Server version	9.6.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
SET @MYSQLDUMP_TEMP_LOG_BIN = @@SESSION.SQL_LOG_BIN;
SET @@SESSION.SQL_LOG_BIN= 0;

--
-- GTID state at the beginning of the backup 
--

SET @@GLOBAL.GTID_PURGED=/*!80000 '+'*/ '4c197a44-2e8c-11f1-bf2e-089798cd1749:1-188';

--
-- Table structure for table `client`
--

DROP TABLE IF EXISTS `client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `client` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `phone` varchar(12) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `telegram` varchar(255) DEFAULT NULL,
  `id_location` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_location` (`id_location`),
  CONSTRAINT `client_ibfk_1` FOREIGN KEY (`id_location`) REFERENCES `location` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `client`
--

LOCK TABLES `client` WRITE;
/*!40000 ALTER TABLE `client` DISABLE KEYS */;
INSERT INTO `client` VALUES (1,'ООО \"Ромашка\"','88005553535','romashka@mail.ru','@romashka',1),(2,'Рога и копыта','79998885544','rogakopyta@google.com','@user12345',2),(3,'Салон Любава','89008003020','lubochka12@yandex.ru','@lubovv1',1),(4,'Котопес','89053452211','kotopes@mail.ru','@kotopes',1),(5,'Металлические конструкции','89553442789','metall@mail.ru','@metallik',2),(6,'Лесопилка','88887775522','lesopilka@yandex.ru','@lesopilka',1);
/*!40000 ALTER TABLE `client` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engineer`
--

DROP TABLE IF EXISTS `engineer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engineer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_user` int NOT NULL,
  `seniority` varchar(255) NOT NULL,
  `weekly_hours` int NOT NULL,
  `workload` int NOT NULL,
  `id_location` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_user` (`id_user`),
  KEY `id_location` (`id_location`),
  CONSTRAINT `engineer_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`),
  CONSTRAINT `engineer_ibfk_2` FOREIGN KEY (`id_location`) REFERENCES `location` (`id`),
  CONSTRAINT `chk_seniority` CHECK ((`seniority` in (_utf8mb4'junior',_utf8mb4'middle',_utf8mb4'senior')))
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engineer`
--

LOCK TABLES `engineer` WRITE;
/*!40000 ALTER TABLE `engineer` DISABLE KEYS */;
INSERT INTO `engineer` VALUES (1,5,'junior',20,8,1),(2,6,'junior',30,6,1),(3,7,'junior',40,6,2),(4,8,'junior',20,0,3),(5,9,'middle',40,8,1),(6,10,'middle',30,5,2),(7,11,'middle',30,0,2),(8,12,'middle',40,0,3),(9,13,'senior',40,0,3),(10,14,'senior',40,9,1),(11,15,'senior',50,8,2),(12,16,'senior',40,0,3),(22,26,'senior',40,7,1);
/*!40000 ALTER TABLE `engineer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engineering_skill`
--

DROP TABLE IF EXISTS `engineering_skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `engineering_skill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_engineer` int NOT NULL,
  `id_skill` int NOT NULL,
  `level` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_engineer` (`id_engineer`,`id_skill`),
  KEY `id_skill` (`id_skill`),
  CONSTRAINT `engineering_skill_ibfk_1` FOREIGN KEY (`id_engineer`) REFERENCES `engineer` (`id`),
  CONSTRAINT `engineering_skill_ibfk_2` FOREIGN KEY (`id_skill`) REFERENCES `skill` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=73 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engineering_skill`
--

LOCK TABLES `engineering_skill` WRITE;
/*!40000 ALTER TABLE `engineering_skill` DISABLE KEYS */;
INSERT INTO `engineering_skill` VALUES (31,1,1,2),(32,1,2,2),(33,1,9,2),(34,2,2,2),(35,2,6,1),(36,2,9,2),(37,3,1,3),(38,3,3,3),(39,3,7,2),(40,4,3,3),(41,4,4,2),(42,4,7,3),(43,5,5,3),(44,5,8,2),(45,5,7,3),(46,6,1,5),(47,6,3,5),(48,6,5,4),(49,6,7,5),(50,7,4,5),(51,7,6,5),(52,7,9,5),(53,7,10,4),(54,8,5,5),(55,8,8,5),(56,8,7,5),(57,9,6,3),(58,9,9,3),(59,9,10,2),(60,10,2,2),(61,10,4,1),(62,10,10,1),(63,11,3,3),(64,11,8,3),(65,11,7,3),(66,12,1,5),(67,12,6,5),(68,12,8,5),(69,12,10,5),(70,22,2,2),(71,22,4,1),(72,22,10,1);
/*!40000 ALTER TABLE `engineering_skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `location` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `city` varchar(255) NOT NULL,
  `street` varchar(255) NOT NULL,
  `house` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Серверная 1','Самара','Самарская',1),(2,'Серверная 2','Самара','Куйбышевская',134),(3,'Узел связи 1','Самара','Короткая',89);
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `requests`
--

DROP TABLE IF EXISTS `requests`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `requests` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_client` int NOT NULL,
  `header` varchar(255) NOT NULL,
  `text` varchar(255) DEFAULT NULL,
  `date` date NOT NULL DEFAULT (curdate()),
  PRIMARY KEY (`id`),
  KEY `id_client` (`id_client`),
  CONSTRAINT `requests_ibfk_1` FOREIGN KEY (`id_client`) REFERENCES `client` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `requests`
--

LOCK TABLES `requests` WRITE;
/*!40000 ALTER TABLE `requests` DISABLE KEYS */;
INSERT INTO `requests` VALUES (1,1,'Не работает сайт','Не загружается сайт, помогите!!','2026-04-30'),(2,2,'Продление SSL','Нужно продлить сертификат. Напишите на почту','2026-04-30'),(3,1,'Настройка копирования','Здравствуйте! Необходимо копировать данные раз в день, а не раз в два дня','2026-04-30'),(4,3,'Новый сайт','Хотим разместить сайт по адресу \"lubava.com\"','2026-04-30'),(5,4,'Много спама','Приходит много спама','2026-04-30'),(6,4,'Размещение нового раздела','Хотим разместить раздел \"Вылеченные животные\"','2026-04-30'),(7,5,'Не работает сайт','Что то сломалось','2026-04-30'),(8,6,'Сломался сайт','Помогите мы теряем деньги сломался сайт','2026-05-07');
/*!40000 ALTER TABLE `requests` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `skill`
--

DROP TABLE IF EXISTS `skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `skill` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `skill`
--

LOCK TABLES `skill` WRITE;
/*!40000 ALTER TABLE `skill` DISABLE KEYS */;
INSERT INTO `skill` VALUES (1,'Администрирование Linux'),(2,'Администрирование Windows'),(3,'Настройка и управление Web-серверами'),(4,'Резервное копирование и восстановление БД'),(5,'Настройка контейнеризации'),(6,'Сетевое администрирование'),(7,'Мониторинг и алертинг'),(8,'Управление облачной инфраструктурой'),(9,'Диагностика и устранение инцидентов'),(10,'Управление доступом и безопасностью');
/*!40000 ALTER TABLE `skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_task_type` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `text` varchar(255) DEFAULT NULL,
  `priority` int NOT NULL,
  `id_engineer` int DEFAULT NULL,
  `status` varchar(80) NOT NULL DEFAULT 'new',
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `completion_time` datetime DEFAULT NULL,
  `estimated_completion_time` datetime DEFAULT NULL,
  `actual_completion_time` datetime DEFAULT NULL,
  `id_location` int NOT NULL,
  `id_request` int NOT NULL,
  `start_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_task_type` (`id_task_type`),
  KEY `id_engineer` (`id_engineer`),
  KEY `id_location` (`id_location`),
  KEY `id_request` (`id_request`),
  CONSTRAINT `task_ibfk_1` FOREIGN KEY (`id_task_type`) REFERENCES `task_type` (`id`),
  CONSTRAINT `task_ibfk_2` FOREIGN KEY (`id_engineer`) REFERENCES `engineer` (`id`),
  CONSTRAINT `task_ibfk_3` FOREIGN KEY (`id_location`) REFERENCES `location` (`id`),
  CONSTRAINT `task_ibfk_4` FOREIGN KEY (`id_request`) REFERENCES `requests` (`id`),
  CONSTRAINT `chk_priority` CHECK ((`priority` in (1,2,3))),
  CONSTRAINT `chk_status` CHECK ((`status` in (_utf8mb4'new',_utf8mb4'process',_utf8mb4'done',_utf8mb4'waiting',_utf8mb4'cancelled')))
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (27,7,'Настройка бэкапа1','text',1,22,'cancelled','2026-05-06 20:00:00','2026-05-07 13:00:00',NULL,NULL,1,1,'2026-05-07 10:00:00'),(28,7,'Настройка бэкапа2','text',2,22,'process','2026-05-06 20:00:00','2026-05-07 16:00:00',NULL,NULL,1,1,'2026-05-07 13:00:00'),(29,7,'Настройка бэкапа3','text',3,10,'cancelled','2026-05-06 20:00:00','2026-05-07 19:00:00',NULL,NULL,1,1,'2026-05-07 16:00:00'),(30,4,'Разместить сайт1','text',1,11,'process','2026-05-06 20:00:00','2026-05-07 12:00:00',NULL,NULL,2,2,'2026-05-07 10:00:00'),(31,2,'asd1','text',1,1,'process','2026-05-06 20:00:00','2026-05-07 18:00:00',NULL,NULL,1,1,'2026-05-07 10:00:00'),(32,7,'Настройка бэкапа1','text',1,10,'process','2026-05-06 20:00:00','2026-05-07 16:00:00',NULL,NULL,1,1,'2026-05-07 13:00:00'),(33,22,'Проверка на спам','Нужно проверить сайт клиента на наличие спам-атак, предпринять меры',1,22,'process','2026-05-06 19:57:15','2026-05-07 18:00:00',NULL,NULL,1,5,'2026-05-07 16:00:00'),(34,13,'Сайт не доступен','описание',1,5,'process','2026-05-06 21:29:23','2026-05-07 13:00:00',NULL,NULL,1,6,'2026-05-07 10:00:00'),(35,8,'Восстановите сайт','Упал сайт',1,10,'process','2026-05-06 21:29:39','2026-05-08 15:00:00',NULL,NULL,1,5,'2026-05-08 10:00:00'),(36,16,'Расширьте дисковое пространство','Мало места',2,5,'process','2026-05-06 21:30:01','2026-05-07 18:00:00',NULL,NULL,1,4,'2026-05-07 13:00:00'),(37,20,'test','test',3,22,'process','2026-05-06 23:03:12','2026-05-07 12:00:00',NULL,NULL,1,3,'2026-05-07 10:00:00'),(38,17,'test','test',2,11,'process','2026-05-06 23:10:25','2026-05-07 16:00:00',NULL,NULL,2,2,'2026-05-07 12:00:00'),(39,22,'test','test',3,10,'process','2026-05-06 23:10:40','2026-05-07 12:00:00',NULL,NULL,1,4,'2026-05-07 10:00:00'),(40,18,'Сломался сайт','Необходимо решить вопрос с работой сайта',1,2,'cancelled','2026-05-07 06:08:13','2026-05-07 13:00:00',NULL,NULL,1,8,'2026-05-07 10:00:00'),(41,18,'Сломался сайт','Решите вопрос с доступом к сайту',1,2,'process','2026-05-07 06:12:42','2026-05-07 13:00:00',NULL,NULL,1,8,'2026-05-07 10:00:00'),(42,18,'test12345','test12345',1,2,'process','2026-05-07 07:13:28','2026-05-07 16:00:00',NULL,NULL,1,1,'2026-05-07 13:00:00');
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_type`
--

DROP TABLE IF EXISTS `task_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `junior_time` int NOT NULL,
  `middle_time` int NOT NULL,
  `senior_time` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_type`
--

LOCK TABLES `task_type` WRITE;
/*!40000 ALTER TABLE `task_type` DISABLE KEYS */;
INSERT INTO `task_type` VALUES (1,'Настройка лимитов и ресурсов',4,3,2),(2,'Подготовка серверов под хостинг',8,7,5),(3,'Настройка Windows Server для клиентов',6,4,2),(4,'Размещение сайтов клиентов',6,5,2),(5,'Подключение SSL-сертификата',4,3,2),(6,'Продление SSL-сертификата',3,1,1),(7,'Настройка регулярных бэкапов',5,3,3),(8,'Быстрое восстановление по запросу',10,6,5),(9,'Проверка целостности бэкапов',2,1,1),(10,'Изоляция контейнеров',7,4,3),(11,'Настройка доменов и DNS-зон',6,5,4),(12,'Работа с NAT',4,3,2),(13,'Мониторинг доступности сайтов',4,3,2),(14,'Настройка уведомлений о сбоях',2,1,1),(15,'Контроль нагрузки и ресурсов',3,2,2),(16,'Управление VPS',7,5,4),(17,'Массовые операции с облачными серверами',6,6,4),(18,'Поиск причины недоступности сайта',3,2,2),(19,'Устранение перезагрузок и падений',5,3,2),(20,'Выдача доступов клиенту',10,5,2),(21,'Настройка изоляции между аккаунтами',3,1,1),(22,'Блокировка подозрительной активности',3,2,2);
/*!40000 ALTER TABLE `task_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task_type_skill`
--

DROP TABLE IF EXISTS `task_type_skill`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task_type_skill` (
  `id_task_type` int NOT NULL,
  `id_skill` int NOT NULL,
  PRIMARY KEY (`id_task_type`,`id_skill`),
  KEY `id_skill` (`id_skill`),
  CONSTRAINT `task_type_skill_ibfk_1` FOREIGN KEY (`id_task_type`) REFERENCES `task_type` (`id`),
  CONSTRAINT `task_type_skill_ibfk_2` FOREIGN KEY (`id_skill`) REFERENCES `skill` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task_type_skill`
--

LOCK TABLES `task_type_skill` WRITE;
/*!40000 ALTER TABLE `task_type_skill` DISABLE KEYS */;
INSERT INTO `task_type_skill` VALUES (1,1),(2,1),(3,2),(4,3),(5,3),(6,3),(7,4),(8,4),(9,4),(10,5),(11,6),(12,6),(13,7),(14,7),(15,7),(16,8),(17,8),(18,9),(19,9),(20,10),(21,10),(22,10);
/*!40000 ALTER TABLE `task_type_skill` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `login` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `lastname` varchar(255) DEFAULT NULL,
  `role` varchar(10) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_created` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `login` (`login`),
  CONSTRAINT `chk_role` CHECK ((`role` in (_utf8mb4'admin',_utf8mb4'dispatcher',_utf8mb4'engineer')))
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','admin123','Александр','Системович','Админов','admin',1,'2026-05-06 19:53:24'),(2,'dispatcher1','pass123','Мария','Игоревна','Соколова','dispatcher',1,'2026-05-06 19:53:24'),(3,'dispatcher2','pass123','Ольга','Петровна','Кузнецова','dispatcher',1,'2026-05-06 19:53:24'),(4,'dispatcher3','pass123','Екатерина','Александровна','Морозова','dispatcher',1,'2026-05-06 19:53:24'),(5,'eng_jun_1','12345','Илья','Сергеевич','Федоров','engineer',1,'2026-05-06 19:53:24'),(6,'eng_jun_2','12345','Дмитрий','Алексеевич','Орлов','engineer',1,'2026-05-06 19:53:24'),(7,'eng_jun_3','12345','Никита','Дмитриевич','Волков','engineer',1,'2026-05-06 19:53:24'),(8,'eng_jun_4','12345','Артем','Игоревич','Лебедев','engineer',1,'2026-05-06 19:53:24'),(9,'eng_mid_1','12345','Сергей','Андреевич','Новиков','engineer',1,'2026-05-06 19:53:24'),(10,'eng_mid_2','12345','Алексей','Иванович','Попов','engineer',1,'2026-05-06 19:53:24'),(11,'eng_mid_3','12345','Роман','Сергеевич','Козлов','engineer',1,'2026-05-06 19:53:24'),(12,'eng_mid_4','12345','Владимир','Олегович','Зайцев','engineer',1,'2026-05-06 19:53:24'),(13,'eng_sen_1','12345','Максим','Андреевич','Павлов','engineer',1,'2026-05-06 19:53:24'),(14,'eng_sen_2','12345','Евгений','Игоревич','Семенов','engineer',1,'2026-05-06 19:53:24'),(15,'eng_sen_3','12345','Константин','Викторович','Голубев','engineer',1,'2026-05-06 19:53:24'),(16,'eng_sen_4','12345','Антон','Павлович','Виноградов','engineer',1,'2026-05-06 19:53:24'),(17,'eng_old_1','12345','Павел','Сергеевич','Белов','engineer',0,'2026-05-06 19:53:24'),(18,'eng_old_2','12345','Юрий','Алексеевич','Титов','engineer',0,'2026-05-06 19:53:24'),(19,'user1','12345','Тимур','Романович','Исаев','dispatcher',1,'2026-05-06 19:53:24'),(20,'user2','12345','Глеб','Ильич','Макаров','engineer',1,'2026-05-06 19:53:24'),(21,'user3','12345','Степан','Андреевич','Денисов','engineer',1,'2026-05-06 19:53:24'),(22,'user4','12345','Арсений','Петрович','Тарасов','engineer',1,'2026-05-06 19:53:24'),(23,'user5','12345','Борис','Игоревич','Щербаков','engineer',1,'2026-05-06 19:53:24'),(24,'user6','12345','Виктор','Сергеевич','Жуков','engineer',1,'2026-05-06 19:53:24'),(25,'user7','12345','Леонид','Александрович','Фролов','engineer',1,'2026-05-06 19:53:24'),(26,'eng_sen_5','12345','Евгений2','Игоревич2','Семенов2','engineer',1,'2026-05-06 19:53:24');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
SET @@SESSION.SQL_LOG_BIN = @MYSQLDUMP_TEMP_LOG_BIN;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-05-11 14:51:16
