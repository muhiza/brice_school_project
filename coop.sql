-- MySQL dump 10.16  Distrib 10.1.29-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: coop
-- ------------------------------------------------------
-- Server version	10.1.29-MariaDB-6

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Assets`
--

DROP TABLE IF EXISTS `Assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assets` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asset_type` varchar(60) DEFAULT NULL,
  `asset_location` varchar(60) DEFAULT NULL,
  `asset_value` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `Assets_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assets`
--

LOCK TABLES `Assets` WRITE;
/*!40000 ALTER TABLE `Assets` DISABLE KEYS */;
INSERT INTO `Assets` VALUES (1,'Inzu','Burera','100000','kkk','juliushirwa@gmail.com'),(2,'Inzu','Burera','100000','jj','juliushirwa@gmail.com');
/*!40000 ALTER TABLE `Assets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `InguzanyoZatanzwe`
--

DROP TABLE IF EXISTS `InguzanyoZatanzwe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `InguzanyoZatanzwe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `InguzanyoZatanzwe_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `InguzanyoZatanzwe_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InguzanyoZatanzwe`
--

LOCK TABLES `InguzanyoZatanzwe` WRITE;
/*!40000 ALTER TABLE `InguzanyoZatanzwe` DISABLE KEYS */;
INSERT INTO `InguzanyoZatanzwe` VALUES (1,6,4,NULL,'2019-02-03 13:23:54','juliushirwa@gmail.com',NULL),(2,5,5,NULL,'2019-02-03 13:27:38','juliushirwa@gmail.com',NULL),(3,400000,500000,NULL,'2019-02-10 14:48:33','juliushirwa@gmail.com',NULL),(4,4000,4000,NULL,'2019-02-18 10:00:38','juliushirwa@gmail.com',7),(5,400000,500000,NULL,'2019-02-18 10:06:43','juliushirwa@gmail.com',8);
/*!40000 ALTER TABLE `InguzanyoZatanzwe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `activities`
--

DROP TABLE IF EXISTS `activities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `activities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `activities_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `activities`
--

LOCK TABLES `activities` WRITE;
/*!40000 ALTER TABLE `activities` DISABLE KEYS */;
/*!40000 ALTER TABLE `activities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('685fa8c7b147');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amatsinda`
--

DROP TABLE IF EXISTS `amatsinda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `amatsinda` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `itsinda_name` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `purpose` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `amatsinda_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amatsinda`
--

LOCK TABLES `amatsinda` WRITE;
/*!40000 ALTER TABLE `amatsinda` DISABLE KEYS */;
INSERT INTO `amatsinda` VALUES (1,'Abahuza','guhuza','guhuza','juliushirwa@gmail.com'),(2,'Abajyanama','kujya inama','itsinda rijya inama','juliushirwa@gmail.com');
/*!40000 ALTER TABLE `amatsinda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `applications`
--

DROP TABLE IF EXISTS `applications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `applications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `emailaa` varchar(200) DEFAULT NULL,
  `firstNameaa` varchar(200) DEFAULT NULL,
  `secondNameaa` varchar(200) DEFAULT NULL,
  `othersaa` varchar(200) DEFAULT NULL,
  `Districtaa` varchar(200) DEFAULT NULL,
  `Sectoraa` varchar(200) DEFAULT NULL,
  `Cellaa` varchar(200) DEFAULT NULL,
  `nIdaa` varchar(200) DEFAULT NULL,
  `entryDateaa` varchar(200) DEFAULT NULL,
  `shareaa` varchar(200) DEFAULT NULL,
  `exitDateaa` varchar(200) DEFAULT NULL,
  `umuzunguraaa` varchar(200) DEFAULT NULL,
  `umukonoaa` varchar(200) DEFAULT NULL,
  `genderaa` varchar(200) DEFAULT NULL,
  `dobaa` varchar(200) DEFAULT NULL,
  `phoneaa` varchar(200) DEFAULT NULL,
  `Amashuriaa` varchar(200) DEFAULT NULL,
  `Ubumugaaa` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `applications_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applications`
--

LOCK TABLES `applications` WRITE;
/*!40000 ALTER TABLE `applications` DISABLE KEYS */;
/*!40000 ALTER TABLE `applications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `applytrainings`
--

DROP TABLE IF EXISTS `applytrainings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `applytrainings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `namea` varchar(200) DEFAULT NULL,
  `abouta` varchar(200) DEFAULT NULL,
  `descriptiona` varchar(200) DEFAULT NULL,
  `datea` varchar(200) DEFAULT NULL,
  `is_activea` tinyint(1) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `applytrainings_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applytrainings`
--

LOCK TABLES `applytrainings` WRITE;
/*!40000 ALTER TABLE `applytrainings` DISABLE KEYS */;
/*!40000 ALTER TABLE `applytrainings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bank`
--

DROP TABLE IF EXISTS `bank`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bank` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `bank_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `bank_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank`
--

LOCK TABLES `bank` WRITE;
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
INSERT INTO `bank` VALUES (1,55,40,NULL,'2019-02-03 13:00:59','juliushirwa@gmail.com',NULL),(2,800000,500000,NULL,'2019-02-10 14:48:20','juliushirwa@gmail.com',NULL),(5,4000,4000,NULL,'2019-02-18 09:31:02','juliushirwa@gmail.com',5),(6,10,4000,NULL,'2019-02-18 09:47:44','juliushirwa@gmail.com',6),(7,860,453,NULL,'2019-02-18 13:21:23','juliushirwa@gmail.com',20);
/*!40000 ALTER TABLE `bank` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bankaccounts`
--

DROP TABLE IF EXISTS `bankaccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bankaccounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `memberId` varchar(200) DEFAULT NULL,
  `memberName` varchar(200) DEFAULT NULL,
  `bankAccountNumber` varchar(200) DEFAULT NULL,
  `accountType` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `bankaccounts_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bankaccounts`
--

LOCK TABLES `bankaccounts` WRITE;
/*!40000 ALTER TABLE `bankaccounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `bankaccounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clients`
--

DROP TABLE IF EXISTS `clients`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clients` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `location` varchar(200) DEFAULT NULL,
  `business` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clients`
--

LOCK TABLES `clients` WRITE;
/*!40000 ALTER TABLE `clients` DISABLE KEYS */;
/*!40000 ALTER TABLE `clients` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `committees`
--

DROP TABLE IF EXISTS `committees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `committees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `nid` varchar(60) DEFAULT NULL,
  `district` varchar(60) DEFAULT NULL,
  `sector` varchar(60) DEFAULT NULL,
  `sex` varchar(60) DEFAULT NULL,
  `yob` varchar(60) DEFAULT NULL,
  `committee` varchar(60) DEFAULT NULL,
  `position` varchar(60) DEFAULT NULL,
  `education` varchar(60) DEFAULT NULL,
  `telephone` varchar(60) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `monthly_net_salary` varchar(60) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `committees_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `committees`
--

LOCK TABLES `committees` WRITE;
/*!40000 ALTER TABLE `committees` DISABLE KEYS */;
/*!40000 ALTER TABLE `committees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communications`
--

DROP TABLE IF EXISTS `communications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `communications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `message` varchar(200) DEFAULT NULL,
  `ms_from` varchar(200) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `to` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `communications_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communications`
--

LOCK TABLES `communications` WRITE;
/*!40000 ALTER TABLE `communications` DISABLE KEYS */;
/*!40000 ALTER TABLE `communications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contributions`
--

DROP TABLE IF EXISTS `contributions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contributions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner` varchar(200) DEFAULT NULL,
  `contributionFor` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `contributions_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `contributions_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contributions`
--

LOCK TABLES `contributions` WRITE;
/*!40000 ALTER TABLE `contributions` DISABLE KEYS */;
/*!40000 ALTER TABLE `contributions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `coopMemberBankAccounts`
--

DROP TABLE IF EXISTS `coopMemberBankAccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `coopMemberBankAccounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `memberName` varchar(100) DEFAULT NULL,
  `bankName` varchar(50) DEFAULT NULL,
  `bankAccountNumber` varchar(50) DEFAULT NULL,
  `umusaruro_resi` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `bankAccountNumber` (`bankAccountNumber`),
  UNIQUE KEY `bankName` (`bankName`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `coopMemberBankAccounts_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `coopMemberBankAccounts_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coopMemberBankAccounts`
--

LOCK TABLES `coopMemberBankAccounts` WRITE;
/*!40000 ALTER TABLE `coopMemberBankAccounts` DISABLE KEYS */;
INSERT INTO `coopMemberBankAccounts` VALUES (1,'Karangwa Hirwa Julien','BK','122213336455',NULL,NULL,'juliushirwa@gmail.com'),(3,'','IM','',NULL,NULL,'juliushirwa@gmail.com'),(7,'Uwitonze Naice','I&M','11111',NULL,NULL,'juliushirwa@gmail.com'),(8,'Muhiza Frank','Equity','215563215',NULL,NULL,'juliushirwa@gmail.com');
/*!40000 ALTER TABLE `coopMemberBankAccounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cooperatives`
--

DROP TABLE IF EXISTS `cooperatives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cooperatives` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cooperatives`
--

LOCK TABLES `cooperatives` WRITE;
/*!40000 ALTER TABLE `cooperatives` DISABLE KEYS */;
/*!40000 ALTER TABLE `cooperatives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `decisions`
--

DROP TABLE IF EXISTS `decisions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `decisions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(200) DEFAULT NULL,
  `decision` varchar(200) DEFAULT NULL,
  `owner` varchar(200) DEFAULT NULL,
  `stakeholders` varchar(200) DEFAULT NULL,
  `due_date` varchar(200) DEFAULT NULL,
  `background` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `decisions_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `decisions`
--

LOCK TABLES `decisions` WRITE;
/*!40000 ALTER TABLE `decisions` DISABLE KEYS */;
/*!40000 ALTER TABLE `decisions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `departments` (
  `id` int(11) DEFAULT NULL,
  `no` int(11) DEFAULT NULL,
  `code` varchar(200) DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  `name` varchar(200) DEFAULT NULL,
  `regdate` varchar(200) DEFAULT NULL,
  `certificate` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `province` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  `sector` varchar(200) DEFAULT NULL,
  `cell` varchar(200) DEFAULT NULL,
  `Activity` varchar(200) DEFAULT NULL,
  `coop_type` varchar(200) DEFAULT NULL,
  `category` varchar(200) DEFAULT NULL,
  `field` varchar(200) DEFAULT NULL,
  `started_data` datetime DEFAULT NULL,
  `starting_share` varchar(200) DEFAULT NULL,
  `share_per_person` varchar(200) DEFAULT NULL,
  `male_members` varchar(200) DEFAULT NULL,
  `female_members` varchar(200) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`email`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (NULL,NULL,NULL,'juliushirwa@gmail.com','KOPETRY',NULL,NULL,NULL,'Kigali City','Gasabo','Bibare','Imanzi','Rice',NULL,NULL,NULL,'2019-01-14 11:38:34','100000','20000','50','30',1),(NULL,NULL,NULL,'naice@gmail.com','CORIMAK',NULL,NULL,NULL,'East','Gatsibo','Gatsibo','Gatsibo','Rice',NULL,NULL,NULL,'2019-02-16 10:22:17','200000','20000','2','1',1);
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(60) DEFAULT NULL,
  `username` varchar(60) DEFAULT NULL,
  `first_name` varchar(60) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `phone_number` varchar(200) DEFAULT NULL,
  `password_hash` varchar(128) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `project_id` int(11) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `cooperative_id` int(11) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  `is_coop_admin` tinyint(1) DEFAULT NULL,
  `is_overall` tinyint(1) DEFAULT NULL,
  `is_invited` tinyint(1) DEFAULT NULL,
  `is_union` tinyint(1) DEFAULT NULL,
  `is_ferwacotamo` tinyint(1) DEFAULT NULL,
  `is_confederation` tinyint(1) DEFAULT NULL,
  `is_rca` tinyint(1) DEFAULT NULL,
  `invited_by` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  KEY `department_id` (`department_id`),
  KEY `employee_id` (`employee_id`),
  KEY `project_id` (`project_id`),
  KEY `role_id` (`role_id`),
  KEY `ix_employees_email` (`email`),
  KEY `ix_employees_first_name` (`first_name`),
  KEY `ix_employees_last_name` (`last_name`),
  KEY `ix_employees_phone_number` (`phone_number`),
  KEY `ix_employees_username` (`username`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `cooperatives` (`id`),
  CONSTRAINT `employees_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `employees_ibfk_3` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`),
  CONSTRAINT `employees_ibfk_4` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`),
  CONSTRAINT `employees_ibfk_5` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'juliushirwa@gmail.com','julien','karangwa hirwa julien',NULL,'0782061714','pbkdf2:sha1:1000$ko5CuuLp$147c18cf20be0d508f105e8497a91f4c1fca1314',NULL,NULL,NULL,NULL,NULL,1,1,0,1,0,0,0,0,'juliushirwa@gmail.com',NULL),(2,'naice@gmail.com','Naice','Mbayire Uwitonze',NULL,'0788347151','pbkdf2:sha1:1000$fRgxFq6u$fde8f993504dd6835e0b4254723c18b664fad71c',NULL,NULL,NULL,NULL,NULL,1,1,0,0,0,0,0,0,NULL,NULL);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `federations`
--

DROP TABLE IF EXISTS `federations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `federations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sno` varchar(200) DEFAULT NULL,
  `code` varchar(200) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `certificate` varchar(200) DEFAULT NULL,
  `reg_date` varchar(200) DEFAULT NULL,
  `province` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  `sector` varchar(200) DEFAULT NULL,
  `activity` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `federations`
--

LOCK TABLES `federations` WRITE;
/*!40000 ALTER TABLE `federations` DISABLE KEYS */;
/*!40000 ALTER TABLE `federations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `files`
--

DROP TABLE IF EXISTS `files`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `files` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `image_filename` varchar(200) DEFAULT NULL,
  `image_url` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `files_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `files`
--

LOCK TABLES `files` WRITE;
/*!40000 ALTER TABLE `files` DISABLE KEYS */;
/*!40000 ALTER TABLE `files` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fixeddepositaccounts`
--

DROP TABLE IF EXISTS `fixeddepositaccounts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `fixeddepositaccounts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `memberId` varchar(200) DEFAULT NULL,
  `memberName` varchar(200) DEFAULT NULL,
  `fixedDepositAmount` varchar(200) DEFAULT NULL,
  `durationInDay` varchar(200) DEFAULT NULL,
  `fixedDepositInterest` varchar(200) DEFAULT NULL,
  `maturityDate` varchar(200) DEFAULT NULL,
  `matureAmount` varchar(200) DEFAULT NULL,
  `createdBy` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fixeddepositaccounts`
--

LOCK TABLES `fixeddepositaccounts` WRITE;
/*!40000 ALTER TABLE `fixeddepositaccounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `fixeddepositaccounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goals`
--

DROP TABLE IF EXISTS `goals`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goals` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `Description` varchar(200) DEFAULT NULL,
  `Amount` varchar(200) DEFAULT NULL,
  `startingDate` varchar(200) DEFAULT NULL,
  `endingDate` varchar(200) DEFAULT NULL,
  `paidMembers` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `goals_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goals`
--

LOCK TABLES `goals` WRITE;
/*!40000 ALTER TABLE `goals` DISABLE KEYS */;
/*!40000 ALTER TABLE `goals` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `howtos`
--

DROP TABLE IF EXISTS `howtos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `howtos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `labels` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `steps` varchar(200) DEFAULT NULL,
  `file` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `howtos_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `howtos`
--

LOCK TABLES `howtos` WRITE;
/*!40000 ALTER TABLE `howtos` DISABLE KEYS */;
/*!40000 ALTER TABLE `howtos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibicuruzwa`
--

DROP TABLE IF EXISTS `ibicuruzwa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibicuruzwa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `ibicuruzwa_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ibicuruzwa_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibicuruzwa`
--

LOCK TABLES `ibicuruzwa` WRITE;
/*!40000 ALTER TABLE `ibicuruzwa` DISABLE KEYS */;
INSERT INTO `ibicuruzwa` VALUES (1,5,4,NULL,'2019-02-03 15:18:31','juliushirwa@gmail.com',NULL),(2,122,4,NULL,'2019-02-03 15:18:31','juliushirwa@gmail.com',NULL),(3,10,1000,NULL,'2019-02-18 11:07:31','juliushirwa@gmail.com',NULL),(4,400000,500000,NULL,'2019-02-18 11:10:23','juliushirwa@gmail.com',19);
/*!40000 ALTER TABLE `ibicuruzwa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibihano`
--

DROP TABLE IF EXISTS `ibihano`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibihano` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AmandeC` int(11) DEFAULT NULL,
  `AmandeApII` int(11) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `ibihano_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ibihano_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibihano`
--

LOCK TABLES `ibihano` WRITE;
/*!40000 ALTER TABLE `ibihano` DISABLE KEYS */;
INSERT INTO `ibihano` VALUES (1,5000,0,'amande',96,'2019-02-16 11:47:22','juliushirwa@gmail.com'),(2,0,0,'',206,'2019-02-16 13:51:36','juliushirwa@gmail.com'),(3,0,0,'',138,'2019-02-16 13:52:49','juliushirwa@gmail.com');
/*!40000 ALTER TABLE `ibihano` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibindi`
--

DROP TABLE IF EXISTS `ibindi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibindi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ImifukaQuantity` int(11) DEFAULT NULL,
  `ImifukaAmount` int(11) DEFAULT NULL,
  `MituelleAmount` int(11) DEFAULT NULL,
  `UmuceriGrade` varchar(100) DEFAULT NULL,
  `UmuceriQuantity` int(11) DEFAULT NULL,
  `UmuceriAmountGrade` int(11) DEFAULT NULL,
  `Avence` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `ibindi_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ibindi_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibindi`
--

LOCK TABLES `ibindi` WRITE;
/*!40000 ALTER TABLE `ibindi` DISABLE KEYS */;
INSERT INTO `ibindi` VALUES (1,4,4000,0,'Grade II',0,0,0,96,'2019-02-16 11:49:41','juliushirwa@gmail.com');
/*!40000 ALTER TABLE `ibindi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibindiRukomatanya`
--

DROP TABLE IF EXISTS `ibindiRukomatanya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibindiRukomatanya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `ibindiRukomatanya_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ibindiRukomatanya_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibindiRukomatanya`
--

LOCK TABLES `ibindiRukomatanya` WRITE;
/*!40000 ALTER TABLE `ibindiRukomatanya` DISABLE KEYS */;
INSERT INTO `ibindiRukomatanya` VALUES (1,15,4,NULL,'2019-02-03 15:46:59','juliushirwa@gmail.com',NULL),(2,10,1000,NULL,'2019-02-18 11:05:30','juliushirwa@gmail.com',16);
/*!40000 ALTER TABLE `ibindiRukomatanya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibiramba`
--

DROP TABLE IF EXISTS `ibiramba`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibiramba` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `ibiramba_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ibiramba_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibiramba`
--

LOCK TABLES `ibiramba` WRITE;
/*!40000 ALTER TABLE `ibiramba` DISABLE KEYS */;
INSERT INTO `ibiramba` VALUES (1,10,4,NULL,'2019-02-03 13:47:44','juliushirwa@gmail.com',NULL),(2,4000,1000,NULL,'2019-02-11 15:20:55','juliushirwa@gmail.com',NULL),(3,400000,50000,NULL,'2019-02-11 18:05:21','juliushirwa@gmail.com',NULL),(4,400000,500000,NULL,'2019-02-18 10:16:03','juliushirwa@gmail.com',9),(5,5225,4111,NULL,'2019-02-18 10:19:28','juliushirwa@gmail.com',10);
/*!40000 ALTER TABLE `ibiramba` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibirarane`
--

DROP TABLE IF EXISTS `ibirarane`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibirarane` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NPKkg` int(11) DEFAULT NULL,
  `NPKPerUnity` int(11) DEFAULT NULL,
  `UREA` int(11) DEFAULT NULL,
  `UREAPerUnity` int(11) DEFAULT NULL,
  `DAP` int(11) DEFAULT NULL,
  `DAPPerUnity` int(11) DEFAULT NULL,
  `KCL` int(11) DEFAULT NULL,
  `KCLPerUnity` int(11) DEFAULT NULL,
  `ImbutoQuantity` float DEFAULT NULL,
  `ImbutoAmount` int(11) DEFAULT NULL,
  `IdeniAmount` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `Briquette` int(11) DEFAULT NULL,
  `BriquettePerUnity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `ibirarane_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ibirarane_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibirarane`
--

LOCK TABLES `ibirarane` WRITE;
/*!40000 ALTER TABLE `ibirarane` DISABLE KEYS */;
INSERT INTO `ibirarane` VALUES (1,0,490,0,340,0,430,0,395,0,400,0,96,'2019-02-16 11:45:34','juliushirwa@gmail.com',0,390),(2,0,490,0,340,0,430,0,395,0,400,0,164,'2019-02-16 13:29:01','juliushirwa@gmail.com',0,390),(3,0,490,0,340,0,430,0,395,0,400,0,232,'2019-02-16 13:51:20','juliushirwa@gmail.com',0,390),(4,0,490,0,340,0,430,0,395,0,400,0,206,'2019-02-16 14:51:51','juliushirwa@gmail.com',0,390);
/*!40000 ALTER TABLE `ibirarane` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibitabobyabanks`
--

DROP TABLE IF EXISTS `ibitabobyabanks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibitabobyabanks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  `igikorwa` varchar(200) DEFAULT NULL,
  `debit` varchar(200) DEFAULT NULL,
  `credit` varchar(200) DEFAULT NULL,
  `solde` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `ibitabobyabanks_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibitabobyabanks`
--

LOCK TABLES `ibitabobyabanks` WRITE;
/*!40000 ALTER TABLE `ibitabobyabanks` DISABLE KEYS */;
/*!40000 ALTER TABLE `ibitabobyabanks` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ibyakoreshejwe`
--

DROP TABLE IF EXISTS `ibyakoreshejwe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ibyakoreshejwe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amazina` varchar(200) DEFAULT NULL,
  `deamAndSup` int(11) DEFAULT NULL,
  `ibihanoCoop` int(11) DEFAULT NULL,
  `APKSAMAKIbihano` int(11) DEFAULT NULL,
  `ibiraraneNPKandUREA` int(11) DEFAULT NULL,
  `umusoroWakarere` int(11) DEFAULT NULL,
  `kwishyuraItsinda` int(11) DEFAULT NULL,
  `sheeting` int(11) DEFAULT NULL,
  `PandS` int(11) DEFAULT NULL,
  `ibyoYagurijwe` int(11) DEFAULT NULL,
  `ibindiYasbwe` int(11) DEFAULT NULL,
  `umusaruro_resi` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `ibyakoreshejwe_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ibyakoreshejwe_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibyakoreshejwe`
--

LOCK TABLES `ibyakoreshejwe` WRITE;
/*!40000 ALTER TABLE `ibyakoreshejwe` DISABLE KEYS */;
/*!40000 ALTER TABLE `ibyakoreshejwe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ikoreshwaRyimari`
--

DROP TABLE IF EXISTS `ikoreshwaRyimari`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ikoreshwaRyimari` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `ikoreshwaRyimari_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ikoreshwaRyimari_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ikoreshwaRyimari`
--

LOCK TABLES `ikoreshwaRyimari` WRITE;
/*!40000 ALTER TABLE `ikoreshwaRyimari` DISABLE KEYS */;
INSERT INTO `ikoreshwaRyimari` VALUES (1,25,4,NULL,'2019-02-03 15:31:37','juliushirwa@gmail.com',NULL),(2,4000,4000,NULL,'2019-02-18 11:07:12','juliushirwa@gmail.com',17);
/*!40000 ALTER TABLE `ikoreshwaRyimari` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inamaubuyobozi`
--

DROP TABLE IF EXISTS `inamaubuyobozi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inamaubuyobozi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(200) DEFAULT NULL,
  `decision` varchar(200) DEFAULT NULL,
  `owner` varchar(200) DEFAULT NULL,
  `stakeholders` varchar(200) DEFAULT NULL,
  `due_date` varchar(200) DEFAULT NULL,
  `background` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `inamaubuyobozi_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inamaubuyobozi`
--

LOCK TABLES `inamaubuyobozi` WRITE;
/*!40000 ALTER TABLE `inamaubuyobozi` DISABLE KEYS */;
/*!40000 ALTER TABLE `inamaubuyobozi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inguzanyozabandi`
--

DROP TABLE IF EXISTS `inguzanyozabandi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inguzanyozabandi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `inguzanyozabandi_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `inguzanyozabandi_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inguzanyozabandi`
--

LOCK TABLES `inguzanyozabandi` WRITE;
/*!40000 ALTER TABLE `inguzanyozabandi` DISABLE KEYS */;
INSERT INTO `inguzanyozabandi` VALUES (1,15,4,NULL,'2019-02-03 15:00:52','juliushirwa@gmail.com',NULL),(2,5,5,NULL,'2019-02-03 15:01:51','juliushirwa@gmail.com',NULL),(4,10,1000,NULL,'2019-02-18 10:50:25','juliushirwa@gmail.com',15);
/*!40000 ALTER TABLE `inguzanyozabandi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inkunga`
--

DROP TABLE IF EXISTS `inkunga`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inkunga` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `inkunga_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `inkunga_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inkunga`
--

LOCK TABLES `inkunga` WRITE;
/*!40000 ALTER TABLE `inkunga` DISABLE KEYS */;
INSERT INTO `inkunga` VALUES (1,14,5,NULL,'2019-02-03 14:34:08','juliushirwa@gmail.com',NULL),(2,500000,400000,NULL,'2019-02-10 14:44:49','juliushirwa@gmail.com',NULL),(3,400000,4000,NULL,'2019-02-18 10:41:16','juliushirwa@gmail.com',13),(4,700,500,NULL,'2019-02-18 13:23:32','juliushirwa@gmail.com',21);
/*!40000 ALTER TABLE `inkunga` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `installments`
--

DROP TABLE IF EXISTS `installments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `installments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `memberId` varchar(200) DEFAULT NULL,
  `loanId` varchar(200) DEFAULT NULL,
  `memberName` varchar(200) DEFAULT NULL,
  `lastInstallmentPay` varchar(200) DEFAULT NULL,
  `lastInstallmentPayDate` varchar(200) DEFAULT NULL,
  `cashOrCheque` varchar(200) DEFAULT NULL,
  `payLoanInstallment` varchar(200) DEFAULT NULL,
  `balance` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  `remarksIfAny` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `installments`
--

LOCK TABLES `installments` WRITE;
/*!40000 ALTER TABLE `installments` DISABLE KEYS */;
/*!40000 ALTER TABLE `installments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `intekorusange`
--

DROP TABLE IF EXISTS `intekorusange`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `intekorusange` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status1` varchar(200) DEFAULT NULL,
  `decision1` varchar(200) DEFAULT NULL,
  `owner1` varchar(200) DEFAULT NULL,
  `stakeholders1` varchar(200) DEFAULT NULL,
  `due_date1` varchar(200) DEFAULT NULL,
  `background1` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `intekorusange_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intekorusange`
--

LOCK TABLES `intekorusange` WRITE;
/*!40000 ALTER TABLE `intekorusange` DISABLE KEYS */;
/*!40000 ALTER TABLE `intekorusange` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inyongeramusaruro`
--

DROP TABLE IF EXISTS `inyongeramusaruro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inyongeramusaruro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NPKkg` int(11) DEFAULT NULL,
  `NPKPerUnity` int(11) DEFAULT NULL,
  `UREA` int(11) DEFAULT NULL,
  `UREAPerUnity` int(11) DEFAULT NULL,
  `DAP` int(11) DEFAULT NULL,
  `DAPPerUnity` int(11) DEFAULT NULL,
  `KCL` int(11) DEFAULT NULL,
  `KCLPerUnity` int(11) DEFAULT NULL,
  `Briquette` int(11) DEFAULT NULL,
  `BriquettePerUnity` int(11) DEFAULT NULL,
  `Cypemetrine` float DEFAULT NULL,
  `Beam` int(11) DEFAULT NULL,
  `ImbutoQuantity` float DEFAULT NULL,
  `ImbutoAmount` int(11) DEFAULT NULL,
  `Redevance` float DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `inyongeramusaruro_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `inyongeramusaruro_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inyongeramusaruro`
--

LOCK TABLES `inyongeramusaruro` WRITE;
/*!40000 ALTER TABLE `inyongeramusaruro` DISABLE KEYS */;
INSERT INTO `inyongeramusaruro` VALUES (1,23,490,32,340,0,430,23,395,22,400,1000,1000,12,400,1200,138,'juliushirwa@gmail.com','2019-02-10 14:05:45'),(2,50,490,25,340,0,430,0,395,0,400,1000,1000,25,400,6433,96,'juliushirwa@gmail.com','2019-02-16 11:37:11'),(3,0,490,0,340,0,430,0,395,0,400,0,0,0,400,0,96,'juliushirwa@gmail.com','2019-02-16 13:50:22');
/*!40000 ALTER TABLE `inyongeramusaruro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `isanduku`
--

DROP TABLE IF EXISTS `isanduku`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `isanduku` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `no` varchar(200) DEFAULT NULL,
  `done_date` varchar(200) DEFAULT NULL,
  `action` varchar(200) DEFAULT NULL,
  `income` varchar(200) DEFAULT NULL,
  `expense` varchar(200) DEFAULT NULL,
  `remain` varchar(200) DEFAULT NULL,
  `done_by` varchar(200) DEFAULT NULL,
  `done_to` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `isanduku_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `isanduku`
--

LOCK TABLES `isanduku` WRITE;
/*!40000 ALTER TABLE `isanduku` DISABLE KEYS */;
/*!40000 ALTER TABLE `isanduku` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `isandukunshya`
--

DROP TABLE IF EXISTS `isandukunshya`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `isandukunshya` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `isandukunshya_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `isandukunshya_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `isandukunshya`
--

LOCK TABLES `isandukunshya` WRITE;
/*!40000 ALTER TABLE `isandukunshya` DISABLE KEYS */;
INSERT INTO `isandukunshya` VALUES (1,10,5,0,'2019-02-03 12:07:30','juliushirwa@gmail.com',NULL),(2,5,5,0,'2019-02-03 16:01:30','juliushirwa@gmail.com',NULL),(3,5,5,0,'2019-02-03 16:55:49','juliushirwa@gmail.com',NULL),(4,4000,1000,0,'2019-02-10 14:30:39','juliushirwa@gmail.com',NULL),(5,400000,300000,0,'2019-02-10 14:48:07','juliushirwa@gmail.com',NULL),(6,50000,20000,0,'2019-02-18 08:28:58','juliushirwa@gmail.com',1),(7,5555,4444,0,'2019-02-18 08:29:38','juliushirwa@gmail.com',2);
/*!40000 ALTER TABLE `isandukunshya` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `itsindamember`
--

DROP TABLE IF EXISTS `itsindamember`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `itsindamember` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) DEFAULT NULL,
  `itsinda_id` int(11) DEFAULT NULL,
  `member_firstname` varchar(200) DEFAULT NULL,
  `member_secondname` varchar(200) DEFAULT NULL,
  `itsinda_name` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `itsinda_id` (`itsinda_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `itsindamember_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `itsindamember_ibfk_2` FOREIGN KEY (`itsinda_id`) REFERENCES `amatsinda` (`id`),
  CONSTRAINT `itsindamember_ibfk_3` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `itsindamember`
--

LOCK TABLES `itsindamember` WRITE;
/*!40000 ALTER TABLE `itsindamember` DISABLE KEYS */;
/*!40000 ALTER TABLE `itsindamember` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links`
--

DROP TABLE IF EXISTS `links`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `link` varchar(200) DEFAULT NULL,
  `title` varchar(200) DEFAULT NULL,
  `labels` varchar(200) DEFAULT NULL,
  `sharewith` varchar(200) DEFAULT NULL,
  `comment` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `links_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links`
--

LOCK TABLES `links` WRITE;
/*!40000 ALTER TABLE `links` DISABLE KEYS */;
/*!40000 ALTER TABLE `links` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loans`
--

DROP TABLE IF EXISTS `loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `loans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `memberId` varchar(200) DEFAULT NULL,
  `memberName` varchar(200) DEFAULT NULL,
  `introducer1Id` varchar(200) DEFAULT NULL,
  `introducer1Name` varchar(200) DEFAULT NULL,
  `introducer1BankAccountBalance` varchar(200) DEFAULT NULL,
  `introducer1Share` varchar(200) DEFAULT NULL,
  `introducer2Id` varchar(200) DEFAULT NULL,
  `introducer2Name` varchar(200) DEFAULT NULL,
  `introducer2BankAccountBalance` varchar(200) DEFAULT NULL,
  `introducer2Share` varchar(200) DEFAULT NULL,
  `loanAmount` varchar(200) DEFAULT NULL,
  `interestRate` varchar(200) DEFAULT NULL,
  `durationInDay` varchar(200) DEFAULT NULL,
  `remarksIfAny` varchar(200) DEFAULT NULL,
  `loanType` varchar(200) DEFAULT NULL,
  `totalLoanWithInterest` varchar(200) DEFAULT NULL,
  `activedBy` varchar(200) DEFAULT NULL,
  `loanIssueDate` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `loans_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loans`
--

LOCK TABLES `loans` WRITE;
/*!40000 ALTER TABLE `loans` DISABLE KEYS */;
/*!40000 ALTER TABLE `loans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `members`
--

DROP TABLE IF EXISTS `members`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `members` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sno` varchar(200) DEFAULT NULL,
  `izina_ribanza` varchar(200) DEFAULT NULL,
  `izina_rikurikira` varchar(200) DEFAULT NULL,
  `Ayandi` varchar(200) DEFAULT NULL,
  `zone` varchar(200) DEFAULT NULL,
  `itsinda` varchar(200) DEFAULT NULL,
  `Igitsina` varchar(200) DEFAULT NULL,
  `Indangamuntu` varchar(200) DEFAULT NULL,
  `tariki_yavukiye` varchar(200) DEFAULT NULL,
  `Intara` varchar(200) DEFAULT NULL,
  `Akarere` varchar(200) DEFAULT NULL,
  `Umurenge` varchar(200) DEFAULT NULL,
  `Akagari` varchar(200) DEFAULT NULL,
  `Umudugudu` varchar(200) DEFAULT NULL,
  `tariki_yinjiriye` varchar(200) DEFAULT NULL,
  `umugabane_ukwezi` varchar(200) DEFAULT NULL,
  `Umukono` varchar(200) DEFAULT NULL,
  `nomero_telephone` varchar(200) DEFAULT NULL,
  `Amashuri` varchar(200) DEFAULT NULL,
  `Ubumuga` varchar(200) DEFAULT NULL,
  `Arubatse` varchar(200) DEFAULT NULL,
  `umubare_abana` varchar(200) DEFAULT NULL,
  `icyiciro_ubudehe` varchar(200) DEFAULT NULL,
  `Ubwishingizi` varchar(200) DEFAULT NULL,
  `akazi_akora_muri_koperative` varchar(200) DEFAULT NULL,
  `akazi_akora_ahandi` varchar(200) DEFAULT NULL,
  `ubuso_ahingaho` varchar(200) DEFAULT NULL,
  `ubwoko_igihingwa` varchar(200) DEFAULT NULL,
  `ubuso_ahingaho_ibindi` varchar(200) DEFAULT NULL,
  `ubwoko_igihingwa_kindi` varchar(200) DEFAULT NULL,
  `ubuso_budakoreshwa` varchar(200) DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `members_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `members_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=375 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
INSERT INTO `members` VALUES (72,'3','Gakunzi    ','Frederique',NULL,NULL,NULL,'male','11 970800913320 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(73,'4','Habarurema   ','Edouard',NULL,NULL,NULL,'male','11 973800959880 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(74,'5','Habyarimana  ','Theogene',NULL,NULL,NULL,'female','11 971800649710 99',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(75,'6','Harorimana  ','Emmanuel',NULL,NULL,NULL,'female','11 990801847110 64',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(76,'7','Havugimana  ','Francois',NULL,NULL,NULL,'female','11 994801140160 19',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(77,'8','Kanyamuhanda   ',' Celestin',NULL,NULL,NULL,'male','11 960800733000 53',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(78,'9','Maniragaba','Samuel',NULL,NULL,NULL,'female','11977801069211 41',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(79,'10','Mujawimana  ',' Consolee',NULL,NULL,NULL,'female','11 966700597410 01',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(80,'11','Mukagasana  ','Dianne',NULL,NULL,NULL,'male','11 962700285500  49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(81,'12','Mukakibibi     ','marie',NULL,NULL,NULL,'male','11 959700606690 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(82,'13','Mukanizeyimana ','Claudette',NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(83,'14','Mukankubito   ','Helene',NULL,NULL,NULL,'male','11 960700644580 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(84,'15','Munyankumburwa   ','Evariste',NULL,NULL,NULL,'male','11 976800909420 10',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(85,'16','Mvuyekure   ',' Evariste',NULL,NULL,NULL,'male','11 976800907090 89',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(86,'17','Niyodusenga  ',' J Damascene',NULL,NULL,NULL,'male','11 990801726580 65',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(87,'18','Niyonsaba   ','Judith',NULL,NULL,NULL,'female','11 985701686450 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(88,'19','Nsengiyumva','Pierre',NULL,NULL,NULL,'female','11  96980068327071',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(89,'20','Ntirenganya   ','Egide',NULL,NULL,NULL,'male','11 989800599650 74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(90,'21','Nyirabarigira   ','Solange',NULL,NULL,NULL,'male','11 990701721860 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(91,'22','Nyirasafari   ','Eulerie',NULL,NULL,NULL,'male','11 946700219940 95',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(92,'23','Sebushumba   ','Theodomile',NULL,NULL,NULL,'female','11 969800647860 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(93,'24','Sibomana    ','Celestin',NULL,NULL,NULL,'female','11 981801456360 11',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(94,'25','Umereweneza /Mukabadahakana',' Venant',NULL,NULL,NULL,'male','11 991801699120 92',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(95,'26','Uwimbabazi',' Claudette',NULL,NULL,NULL,'female','11  98470173689096',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(96,'29','Ayinkamiye  ','Angelique',NULL,NULL,NULL,'male','1 197970 1162 550 31',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(97,'30','Batamuriza','Alphonsine',NULL,NULL,NULL,'male','11 982701769266 54',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(98,'31','Buhigiro  ','Pierre',NULL,NULL,NULL,'female','11 94080024486 030',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(99,'32','Buhinja','Eric',NULL,NULL,NULL,'male','11  988800663820 81',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(100,'33','Hagenimana  ','Innocent',NULL,NULL,NULL,'male','11 98080163251 003',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(101,'34','Hitimana  ','Ferdinand',NULL,NULL,NULL,'female','11 977800830620 59',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(102,'35','Iradukunda','Eric',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(103,'36','Iyamuremye    ','Augustin',NULL,NULL,NULL,'male','11 959800696410 76',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(104,'37','Kagoyire   ','Jeanne',NULL,NULL,NULL,'male','11976700907120  74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(105,'38','Karegeya  ','Alexandre',NULL,NULL,NULL,'female','11 975800887350 39',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(106,'39','Karuhije','Pascal',NULL,NULL,NULL,'female','11 946800171340 98',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(107,'40','Mazimpaka  ','Patrique',NULL,NULL,NULL,'male','11 985801114200 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(108,'41','Mupagasi    ','Venant',NULL,NULL,NULL,'male','11 954800414790 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(109,'42','Musabyimana','Delphine',NULL,NULL,NULL,'male','11 974700900580 35',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(110,'43','Nsengiyumva','J Baptiste',NULL,NULL,NULL,'female','11  981801415140 12',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(111,'44','Nsengiyumva ','Elisse',NULL,NULL,NULL,'male','11 966800273706 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(112,'45','Nsengumuremyi','Joel',NULL,NULL,NULL,'female','11 979800515331 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(113,'46','Nyandwi   ','Léonard',NULL,NULL,NULL,'female','11 958800226560 20',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(114,'47','Nyirandabananiye  ','Alphonsine',NULL,NULL,NULL,'male','11 984700732530 62',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(115,'48','Nyiranizeye','Monique',NULL,NULL,NULL,'male','11  97870050150044',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(116,'49','Nyiransabimana  ','Madina',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(117,'50','Nyirarudodo   ',' Alphonsine',NULL,NULL,NULL,'female','11 962700694560 68',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(118,'51','Nzamuturayezu    ','Dismas',NULL,NULL,NULL,'male','11 962800694570 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(119,'52','Rwakibibi','Valens',NULL,NULL,NULL,'male','11 979801031270 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(120,'53','Uwimana','Theopiste',NULL,NULL,NULL,'male','11  98270186019017',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(121,'55','Gahunde   ','Jean',NULL,NULL,NULL,'male','11 968800719940 26',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(122,'56','Habihirwe    ','Simeon',NULL,NULL,NULL,'male','11 984800879432 14',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(123,'57','Hagumamahoro     ','Egide',NULL,NULL,NULL,'male','11 98680137191 109',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(124,'58','Kanyamacumbi','Frederic',NULL,NULL,NULL,'female','11982 80023838004',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(125,'59','Mbarushimana  ',' J M Vianney',NULL,NULL,NULL,'male','11 982801754051 36',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(126,'60','Minani ',' J Baptiste',NULL,NULL,NULL,'male','11  97580023711019',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(127,'61','Mugeni','Speciose',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(128,'62','Mukamulisa','Esperance',NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(129,'63','Mukandagijimana   ','Marie',NULL,NULL,NULL,'female','11 965700582720 22',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(130,'64','Ndayisenga   ','Olivier',NULL,NULL,NULL,'female','11 984800443450 48',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(131,'65','Ndikubwimana ','J Chrisostome',NULL,NULL,NULL,'female','11 965800649250 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(132,'66','Nirere    ','Chartine',NULL,NULL,NULL,'male','11  9770097935014',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(133,'67','Niyonshima    ','Saidate',NULL,NULL,NULL,'male','11 962700694890 93',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(134,'68','Nyirarekeraho   ','Donatille',NULL,NULL,NULL,'female','11 974700901070 97',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(135,'69','Rubimbura   ','Charles',NULL,NULL,NULL,'female','11 972800860691 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(137,'71','Sibomana     ','Theoneste',NULL,NULL,NULL,'male','11 984800166061 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(138,'1','Ahimana ','Thicien',NULL,NULL,NULL,'male','11  98380155023009',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,'2000',NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(139,'2','Bantegeye    ','Florence',NULL,NULL,NULL,'male','11 984701704220 10',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(140,'3','Gakunzi    ','Frederique',NULL,NULL,NULL,'male','11 970800913320 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(141,'4','Habarurema   ','Edouard',NULL,NULL,NULL,'male','11 973800959880 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(142,'5','Habyarimana  ','Theogene',NULL,NULL,NULL,'female','11 971800649710 99',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(143,'6','Harorimana  ','Emmanuel',NULL,NULL,NULL,'female','11 990801847110 64',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(144,'7','Havugimana  ','Francois',NULL,NULL,NULL,'female','11 994801140160 19',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(145,'8','Kanyamuhanda   ',' Celestin',NULL,NULL,NULL,'male','11 960800733000 53',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(146,'9','Maniragaba','Samuel',NULL,NULL,NULL,'female','11977801069211 41',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(147,'10','Mujawimana  ',' Consolee',NULL,NULL,NULL,'female','11 966700597410 01',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(148,'11','Mukagasana  ','Dianne',NULL,NULL,NULL,'male','11 962700285500  49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(149,'12','Mukakibibi     ','marie',NULL,NULL,NULL,'male','11 959700606690 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(150,'13','Mukanizeyimana ','Claudette',NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(151,'14','Mukankubito   ','Helene',NULL,NULL,NULL,'male','11 960700644580 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(152,'15','Munyankumburwa   ','Evariste',NULL,NULL,NULL,'male','11 976800909420 10',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(153,'16','Mvuyekure   ',' Evariste',NULL,NULL,NULL,'male','11 976800907090 89',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(154,'17','Niyodusenga  ',' J Damascene',NULL,NULL,NULL,'male','11 990801726580 65',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(155,'18','Niyonsaba   ','Judith',NULL,NULL,NULL,'female','11 985701686450 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(156,'19','Nsengiyumva','Pierre',NULL,NULL,NULL,'female','11  96980068327071',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(157,'20','Ntirenganya   ','Egide',NULL,NULL,NULL,'male','11 989800599650 74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(158,'21','Nyirabarigira   ','Solange',NULL,NULL,NULL,'male','11 990701721860 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(159,'22','Nyirasafari   ','Eulerie',NULL,NULL,NULL,'male','11 946700219940 95',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(160,'23','Sebushumba   ','Theodomile',NULL,NULL,NULL,'female','11 969800647860 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(161,'24','Sibomana    ','Celestin',NULL,NULL,NULL,'female','11 981801456360 11',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(162,'25','Umereweneza /Mukabadahakana',' Venant',NULL,NULL,NULL,'male','11 991801699120 92',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(163,'26','Uwimbabazi',' Claudette',NULL,NULL,NULL,'female','11  98470173689096',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(164,'29','Ayinkamiye  ','Angelique',NULL,NULL,NULL,'male','1 197970 1162 550 31',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(165,'30','Batamuriza','Alphonsine',NULL,NULL,NULL,'male','11 982701769266 54',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(166,'31','Buhigiro  ','Pierre',NULL,NULL,NULL,'female','11 94080024486 030',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(167,'32','Buhinja','Eric',NULL,NULL,NULL,'male','11  988800663820 81',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(168,'33','Hagenimana  ','Innocent',NULL,NULL,NULL,'male','11 98080163251 003',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(169,'34','Hitimana  ','Ferdinand',NULL,NULL,NULL,'female','11 977800830620 59',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(170,'35','Iradukunda','Eric',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(171,'36','Iyamuremye    ','Augustin',NULL,NULL,NULL,'male','11 959800696410 76',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(172,'37','Kagoyire   ','Jeanne',NULL,NULL,NULL,'male','11976700907120  74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(173,'38','Karegeya  ','Alexandre',NULL,NULL,NULL,'female','11 975800887350 39',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(174,'39','Karuhije','Pascal',NULL,NULL,NULL,'female','11 946800171340 98',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(175,'40','Mazimpaka  ','Patrique',NULL,NULL,NULL,'male','11 985801114200 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(176,'41','Mupagasi    ','Venant',NULL,NULL,NULL,'male','11 954800414790 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(177,'42','Musabyimana','Delphine',NULL,NULL,NULL,'male','11 974700900580 35',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(178,'43','Nsengiyumva','J Baptiste',NULL,NULL,NULL,'female','11  981801415140 12',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(179,'44','Nsengiyumva ','Elisse',NULL,NULL,NULL,'male','11 966800273706 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(180,'45','Nsengumuremyi','Joel',NULL,NULL,NULL,'female','11 979800515331 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(181,'46','Nyandwi   ','Léonard',NULL,NULL,NULL,'female','11 958800226560 20',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(182,'47','Nyirandabananiye  ','Alphonsine',NULL,NULL,NULL,'male','11 984700732530 62',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(183,'48','Nyiranizeye','Monique',NULL,NULL,NULL,'male','11  97870050150044',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(184,'49','Nyiransabimana  ','Madina',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(185,'50','Nyirarudodo   ',' Alphonsine',NULL,NULL,NULL,'female','11 962700694560 68',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(186,'51','Nzamuturayezu    ','Dismas',NULL,NULL,NULL,'male','11 962800694570 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(187,'52','Rwakibibi','Valens',NULL,NULL,NULL,'male','11 979801031270 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(188,'53','Uwimana','Theopiste',NULL,NULL,NULL,'male','11  98270186019017',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(189,'55','Gahunde   ','Jean',NULL,NULL,NULL,'male','11 968800719940 26',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(190,'56','Habihirwe    ','Simeon',NULL,NULL,NULL,'male','11 984800879432 14',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(191,'57','Hagumamahoro     ','Egide',NULL,NULL,NULL,'male','11 98680137191 109',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(192,'58','Kanyamacumbi','Frederic',NULL,NULL,NULL,'female','11982 80023838004',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(193,'59','Mbarushimana  ',' J M Vianney',NULL,NULL,NULL,'male','11 982801754051 36',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(194,'60','Minani ',' J Baptiste',NULL,NULL,NULL,'male','11  97580023711019',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(195,'61','Mugeni','Speciose',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(196,'62','Mukamulisa','Esperance',NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(197,'63','Mukandagijimana   ','Marie',NULL,NULL,NULL,'female','11 965700582720 22',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(198,'64','Ndayisenga   ','Olivier',NULL,NULL,NULL,'female','11 984800443450 48',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(199,'65','Ndikubwimana ','J Chrisostome',NULL,NULL,NULL,'female','11 965800649250 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(200,'66','Nirere    ','Chartine',NULL,NULL,NULL,'male','11  9770097935014',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(201,'67','Niyonshima    ','Saidate',NULL,NULL,NULL,'male','11 962700694890 93',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(202,'68','Nyirarekeraho   ','Donatille',NULL,NULL,NULL,'female','11 974700901070 97',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(203,'69','Rubimbura   ','Charles',NULL,NULL,NULL,'female','11 972800860691 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(205,'71','Sibomana     ','Theoneste',NULL,NULL,NULL,'male','11 984800166061 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(206,'1','Ahimana ','Thicien',NULL,NULL,NULL,'male','11  98380155023009',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,'2000',NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(207,'2','Bantegeye    ','Florence',NULL,NULL,NULL,'male','11 984701704220 10',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(208,'3','Gakunzi    ','Frederique',NULL,NULL,NULL,'male','11 970800913320 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(209,'4','Habarurema   ','Edouard',NULL,NULL,NULL,'male','11 973800959880 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(210,'5','Habyarimana  ','Theogene',NULL,NULL,NULL,'female','11 971800649710 99',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(211,'6','Harorimana  ','Emmanuel',NULL,NULL,NULL,'female','11 990801847110 64',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(212,'7','Havugimana  ','Francois',NULL,NULL,NULL,'female','11 994801140160 19',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(213,'8','Kanyamuhanda   ',' Celestin',NULL,NULL,NULL,'male','11 960800733000 53',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(214,'9','Maniragaba','Samuel',NULL,NULL,NULL,'female','11977801069211 41',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(215,'10','Mujawimana  ',' Consolee',NULL,NULL,NULL,'female','11 966700597410 01',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(216,'11','Mukagasana  ','Dianne',NULL,NULL,NULL,'male','11 962700285500  49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(217,'12','Mukakibibi     ','marie',NULL,NULL,NULL,'male','11 959700606690 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(218,'13','Mukanizeyimana ','Claudette',NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(219,'14','Mukankubito   ','Helene',NULL,NULL,NULL,'male','11 960700644580 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(220,'15','Munyankumburwa   ','Evariste',NULL,NULL,NULL,'male','11 976800909420 10',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(221,'16','Mvuyekure   ',' Evariste',NULL,NULL,NULL,'male','11 976800907090 89',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(222,'17','Niyodusenga  ',' J Damascene',NULL,NULL,NULL,'male','11 990801726580 65',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(223,'18','Niyonsaba   ','Judith',NULL,NULL,NULL,'female','11 985701686450 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(224,'19','Nsengiyumva','Pierre',NULL,NULL,NULL,'female','11  96980068327071',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(225,'20','Ntirenganya   ','Egide',NULL,NULL,NULL,'male','11 989800599650 74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(226,'21','Nyirabarigira   ','Solange',NULL,NULL,NULL,'male','11 990701721860 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(227,'22','Nyirasafari   ','Eulerie',NULL,NULL,NULL,'male','11 946700219940 95',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(228,'23','Sebushumba   ','Theodomile',NULL,NULL,NULL,'female','11 969800647860 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(229,'24','Sibomana    ','Celestin',NULL,NULL,NULL,'female','11 981801456360 11',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(230,'25','Umereweneza /Mukabadahakana',' Venant',NULL,NULL,NULL,'male','11 991801699120 92',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(231,'26','Uwimbabazi',' Claudette',NULL,NULL,NULL,'female','11  98470173689096',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(232,'29','Ayinkamiye  ','Angelique',NULL,NULL,NULL,'male','1 197970 1162 550 31',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(233,'30','Batamuriza','Alphonsine',NULL,NULL,NULL,'male','11 982701769266 54',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(234,'31','Buhigiro  ','Pierre',NULL,NULL,NULL,'female','11 94080024486 030',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(235,'32','Buhinja','Eric',NULL,NULL,NULL,'male','11  988800663820 81',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(236,'33','Hagenimana  ','Innocent',NULL,NULL,NULL,'male','11 98080163251 003',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(237,'34','Hitimana  ','Ferdinand',NULL,NULL,NULL,'female','11 977800830620 59',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(238,'35','Iradukunda','Eric',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(239,'36','Iyamuremye    ','Augustin',NULL,NULL,NULL,'male','11 959800696410 76',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(240,'37','Kagoyire   ','Jeanne',NULL,NULL,NULL,'male','11976700907120  74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(241,'38','Karegeya  ','Alexandre',NULL,NULL,NULL,'female','11 975800887350 39',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(242,'39','Karuhije','Pascal',NULL,NULL,NULL,'female','11 946800171340 98',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(243,'40','Mazimpaka  ','Patrique',NULL,NULL,NULL,'male','11 985801114200 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(244,'41','Mupagasi    ','Venant',NULL,NULL,NULL,'male','11 954800414790 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(245,'42','Musabyimana','Delphine',NULL,NULL,NULL,'male','11 974700900580 35',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(246,'43','Nsengiyumva','J Baptiste',NULL,NULL,NULL,'female','11  981801415140 12',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(247,'44','Nsengiyumva ','Elisse',NULL,NULL,NULL,'male','11 966800273706 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(248,'45','Nsengumuremyi','Joel',NULL,NULL,NULL,'female','11 979800515331 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(249,'46','Nyandwi   ','Léonard',NULL,NULL,NULL,'female','11 958800226560 20',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(250,'47','Nyirandabananiye  ','Alphonsine',NULL,NULL,NULL,'male','11 984700732530 62',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(251,'48','Nyiranizeye','Monique',NULL,NULL,NULL,'male','11  97870050150044',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(252,'49','Nyiransabimana  ','Madina',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(253,'50','Nyirarudodo   ',' Alphonsine',NULL,NULL,NULL,'female','11 962700694560 68',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(254,'51','Nzamuturayezu    ','Dismas',NULL,NULL,NULL,'male','11 962800694570 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(255,'52','Rwakibibi','Valens',NULL,NULL,NULL,'male','11 979801031270 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(256,'53','Uwimana','Theopiste',NULL,NULL,NULL,'male','11  98270186019017',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(257,'55','Gahunde   ','Jean',NULL,NULL,NULL,'male','11 968800719940 26',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(258,'56','Habihirwe    ','Simeon',NULL,NULL,NULL,'male','11 984800879432 14',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(259,'57','Hagumamahoro     ','Egide',NULL,NULL,NULL,'male','11 98680137191 109',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(260,'58','Kanyamacumbi','Frederic',NULL,NULL,NULL,'female','11982 80023838004',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(261,'59','Mbarushimana  ',' J M Vianney',NULL,NULL,NULL,'male','11 982801754051 36',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(262,'60','Minani ',' J Baptiste',NULL,NULL,NULL,'male','11  97580023711019',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(263,'61','Mugeni','Speciose',NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(264,'62','Mukamulisa','Esperance',NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(265,'63','Mukandagijimana   ','Marie',NULL,NULL,NULL,'female','11 965700582720 22',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(266,'64','Ndayisenga   ','Olivier',NULL,NULL,NULL,'female','11 984800443450 48',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(267,'65','Ndikubwimana ','J Chrisostome',NULL,NULL,NULL,'female','11 965800649250 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(268,'66','Nirere    ','Chartine',NULL,NULL,NULL,'male','11  9770097935014',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(269,'67','Niyonshima    ','Saidate',NULL,NULL,NULL,'male','11 962700694890 93',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(270,'68','Nyirarekeraho   ','Donatille',NULL,NULL,NULL,'female','11 974700901070 97',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(271,'69','Rubimbura   ','Charles',NULL,NULL,NULL,'female','11 972800860691 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(273,'71','Sibomana     ','Theoneste',NULL,NULL,NULL,'male','11 984800166061 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'juliushirwa@gmail.com'),(274,'1','Imanishimwe ',NULL,NULL,NULL,NULL,'male','11  98380155023009',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,'2000',NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(275,'2','KARUHIJE pascal',NULL,NULL,NULL,NULL,'male','11 984701704220 10',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(276,'3','Ayinkamiye Angelique',NULL,NULL,NULL,NULL,'male','11 970800913320 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(277,'4','Nyirandabananiye Alphonsine',NULL,NULL,NULL,NULL,'male','11 973800959880 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(278,'5','Niyibizi Bosco',NULL,NULL,NULL,NULL,'female','11 971800649710 99',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(279,'6','Kanyamuhanda Celestin',NULL,NULL,NULL,NULL,'female','11 990801847110 64',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(280,'7','Sibomana J. Pierre',NULL,NULL,NULL,NULL,'female','11 994801140160 19',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(281,'8','Nywandwi Leonard',NULL,NULL,NULL,NULL,'male','11 960800733000 53',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(282,'9','Musabyimana Delphine',NULL,NULL,NULL,NULL,'female','11977801069211 41',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(283,'10','Nsengiyumva J Baptiste',NULL,NULL,NULL,NULL,'female','11 966700597410 01',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(284,'11','Ruhinja Eric',NULL,NULL,NULL,NULL,'male','11 962700285500  49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(285,'12','Nsengiyumva Elise',NULL,NULL,NULL,NULL,'male','11 959700606690 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(286,'13','Nzamuturayezu Dismas',NULL,NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(287,'14','Nyirarudodo Alphonsine',NULL,NULL,NULL,NULL,'male','11 960700644580 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(288,'15','Nsengumuremyi Joel',NULL,NULL,NULL,NULL,'male','11 976800909420 10',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(289,'16','Kagoyire jeanne',NULL,NULL,NULL,NULL,'male','11 976800907090 89',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(290,'17','Rwakibibi Valens',NULL,NULL,NULL,NULL,'male','11 990801726580 65',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(291,'18','Buhigiro Pierre',NULL,NULL,NULL,NULL,'female','11 985701686450 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(292,'19','Iyamuremye Augustin',NULL,NULL,NULL,NULL,'female','11  96980068327071',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(293,'20','Karegeya Alexendre',NULL,NULL,NULL,NULL,'male','11 989800599650 74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(294,'21','Batamuriza Alphonsine',NULL,NULL,NULL,NULL,'male','11 990701721860 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(295,'22','Hagenimana Innocent',NULL,NULL,NULL,NULL,'male','11 946700219940 95',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(296,'23','Mazimpaka Patrick',NULL,NULL,NULL,NULL,'female','11 969800647860 08',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(297,'24','Nyiransabimana Madina',NULL,NULL,NULL,NULL,'female','11 981801456360 11',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(298,'25','Hitimana ferdinard',NULL,NULL,NULL,NULL,'male','11 991801699120 92',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(299,'26','Mupagasi Venant',NULL,NULL,NULL,NULL,'female','11  98470173689096',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(300,'29','Zone kiramuruzi',NULL,NULL,NULL,NULL,'male','1 197970 1162 550 31',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(301,'30','Rubimbura Charles',NULL,NULL,NULL,NULL,'male','11 982701769266 54',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(302,'31','Muhizi Elie',NULL,NULL,NULL,NULL,'female','11 94080024486 030',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(303,'32','Munyemana Frodouard',NULL,NULL,NULL,NULL,'male','11  988800663820 81',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(304,'33','Bantegeye Florance',NULL,NULL,NULL,NULL,'male','11 98080163251 003',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','amaguru',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(305,'34','Mukagasana Dianne',NULL,NULL,NULL,NULL,'female','11 977800830620 59',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(306,'35','Habuhazi J. Bosco',NULL,NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none ',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(307,'36','Niyonzima Emmanuel',NULL,NULL,NULL,NULL,'male','11 959800696410 76',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(308,'37','Habyarimana Michel',NULL,NULL,NULL,NULL,'male','11976700907120  74',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(309,'38','Ntirivamunda justin',NULL,NULL,NULL,NULL,'female','11 975800887350 39',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(310,'39','NDAGIJE/ Choral Jeovaire',NULL,NULL,NULL,NULL,'female','11 946800171340 98',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(311,'40','Nikiza Gribert',NULL,NULL,NULL,NULL,'male','11 985801114200 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(312,'41','Hakizimana j Pierre',NULL,NULL,NULL,NULL,'male','11 954800414790 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(313,'42','Gasore j. de Dieu',NULL,NULL,NULL,NULL,'male','11 974700900580 35',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(314,'43','Ngendahimana Pascal',NULL,NULL,NULL,NULL,'female','11  981801415140 12',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(315,'44','Mukantibagirirwa Venantien',NULL,NULL,NULL,NULL,'male','11 966800273706 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(316,'45','Imanishimwe ',NULL,NULL,NULL,NULL,'female','11 979800515331 50',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(317,'46','KARUHIJE pascal',NULL,NULL,NULL,NULL,'female','11 958800226560 20',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(318,'47','Ayinkamiye Angelique',NULL,NULL,NULL,NULL,'male','11 984700732530 62',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(319,'48','Nyirandabananiye Alphonsine',NULL,NULL,NULL,NULL,'male','11  97870050150044',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(320,'49','Niyibizi Bosco',NULL,NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(321,'50','Kanyamuhanda Celestin',NULL,NULL,NULL,NULL,'female','11 962700694560 68',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(322,'51','Sibomana J. Pierre',NULL,NULL,NULL,NULL,'male','11 962800694570 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(323,'52','Nywandwi Leonard',NULL,NULL,NULL,NULL,'male','11 979801031270 15',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(324,'53','Musabyimana Delphine',NULL,NULL,NULL,NULL,'male','11  98270186019017',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(325,'55','Nsanzumuhire Mathiase',NULL,NULL,NULL,NULL,'male','11 968800719940 26',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(326,'56','Nsabimana Emmanuel',NULL,NULL,NULL,NULL,'male','11 984800879432 14',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(327,'57','Musabyemariya Francoise',NULL,NULL,NULL,NULL,'male','11 98680137191 109',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(328,'58','Karegeya Emmanuel',NULL,NULL,NULL,NULL,'female','11982 80023838004',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(329,'59','Singirankabo J.M.V',NULL,NULL,NULL,NULL,'male','11 982801754051 36',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(330,'60','Mugabire Dieudonne',NULL,NULL,NULL,NULL,'male','11  97580023711019',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(331,'61','Muvunyi Dominique',NULL,NULL,NULL,NULL,'male',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(332,'62','Rwamakuba Gabriel',NULL,NULL,NULL,NULL,'female',NULL,NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(333,'63','Manirumva Celestin',NULL,NULL,NULL,NULL,'female','11 965700582720 22',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(334,'64','Nyirabahire Felecite',NULL,NULL,NULL,NULL,'female','11 984800443450 48',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(335,'65','Butera Eliase',NULL,NULL,NULL,NULL,'female','11 965800649250 91',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(336,'66','Uwera Madia',NULL,NULL,NULL,NULL,'male','11  9770097935014',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'NA','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(337,'67','Habineza Djuma',NULL,NULL,NULL,NULL,'male','11 962700694890 93',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'low','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(338,'68','Amizero Cyprien',NULL,NULL,NULL,NULL,'female','11 974700901070 97',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'no','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(339,'69','Habineza Djuma',NULL,NULL,NULL,NULL,'female','11 972800860691 49',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(340,'70','Mukadusabe Dina',NULL,NULL,NULL,NULL,'female','11 993800639440 81',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'high','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(341,'71','Seminega Frodouard',NULL,NULL,NULL,NULL,'male','11 984800166061 43',NULL,'East','Gatsibo',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'medium','none',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(342,NULL,'Karisa Anastase',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(343,NULL,'Karegeya Emmanuel',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(344,NULL,'Nyiraruhinja Alphonsine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(345,NULL,'Ngwabije j. Bosco',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(346,NULL,'Musanabandi Marie',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(347,NULL,'Habagusenga Ananiase',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(348,NULL,'Uwimbabazi Claudette',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(349,NULL,'Karegeya Emmanuel',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(350,NULL,'Gasore j. de Dieu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(351,NULL,'Sibomana Faustin',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(352,NULL,'Baracyandebera jean',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(353,NULL,'Ndorimana J. Pierre',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(354,NULL,'Ndorimana J. Pierre',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(355,NULL,'Habyarimana Michel',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(356,NULL,'Munyemana J. Dieu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(357,NULL,'Musengamana J .Damascene',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(358,NULL,'Ntakirutimana Joel',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(359,NULL,'Ntakirutimana Joel',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(360,NULL,'Sibomana Jean',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(361,NULL,'Ntezimana Eduard',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(362,NULL,'Nyirabaribeshya Donatha',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(363,NULL,'Mukamana Josepha',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(364,NULL,'Mukagihana Charlotte',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(365,NULL,'Sebigirimana Onesphole',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(366,NULL,'Gahinda Gaspard',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(367,NULL,'Mbonyumuvunyi Jacque',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(368,NULL,'Burengero Theogene',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(369,NULL,'Gasore j. de Dieu',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(370,NULL,'Nyiransabimana Vestine',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(371,NULL,'Biseruka Augustin',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(372,NULL,'Mushinzimana Charles',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(373,NULL,'Maniraguha Isaac',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com'),(374,NULL,'Nyiraruugwiro Providance',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,'naice@gmail.com');
/*!40000 ALTER TABLE `members` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `motos`
--

DROP TABLE IF EXISTS `motos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `motos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `plate` varchar(200) DEFAULT NULL,
  `owner` varchar(200) DEFAULT NULL,
  `owner_tel` varchar(200) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `motos_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `motos_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motos`
--

LOCK TABLES `motos` WRITE;
/*!40000 ALTER TABLE `motos` DISABLE KEYS */;
/*!40000 ALTER TABLE `motos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action` varchar(200) DEFAULT NULL,
  `done_by` varchar(200) DEFAULT NULL,
  `done_from` varchar(200) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  `done_time` varchar(200) DEFAULT NULL,
  `done_to` varchar(200) DEFAULT NULL,
  `effect` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=65 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,'Created account','julien','127.0.1.1','2019-01-14 11:37:50','frank','tapayi','system upgraded',NULL),(2,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-14 11:38:01','frank','tapayi','system upgraded',NULL),(3,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-14 11:38:43','frank','tapayi','system upgraded',NULL),(4,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-14 11:49:29','frank','tapayi','system upgraded',NULL),(5,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-14 13:25:23','frank','tapayi','system upgraded',NULL),(6,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-14 14:22:13','frank','tapayi','system upgraded',NULL),(7,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-14 15:37:59','frank','tapayi','system upgraded',NULL),(8,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-14 15:48:18','frank','tapayi','system upgraded',NULL),(9,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-15 07:34:22','frank','tapayi','system upgraded',NULL),(10,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-30 12:28:01','frank','tapayi','system upgraded',NULL),(11,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-30 15:55:57','frank','tapayi','system upgraded',NULL),(12,'Logged out','julien','127.0.1.1','2019-01-30 15:56:44','frank','tapayi','system upgraded',NULL),(13,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-30 15:57:14','frank','tapayi','system upgraded',NULL),(14,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-30 16:09:49','frank','tapayi','system upgraded',NULL),(15,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-30 17:59:49','frank','tapayi','system upgraded',NULL),(16,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-30 18:22:26','frank','tapayi','system upgraded',NULL),(17,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-30 18:23:42','frank','tapayi','system upgraded',NULL),(18,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-31 02:51:43','frank','tapayi','system upgraded',NULL),(19,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-01-31 14:49:36','frank','tapayi','system upgraded',NULL),(20,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-01 08:57:07','frank','tapayi','system upgraded',NULL),(21,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-02 10:56:09','frank','tapayi','system upgraded',NULL),(22,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-03 07:14:41','frank','tapayi','system upgraded',NULL),(23,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-03 11:13:43','frank','tapayi','system upgraded',NULL),(24,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-03 17:10:33','frank','tapayi','system upgraded',NULL),(25,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-03 23:04:37','frank','tapayi','system upgraded',NULL),(26,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-04 06:34:55','frank','tapayi','system upgraded',NULL),(27,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-05 05:44:26','frank','tapayi','system upgraded',NULL),(28,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-05 11:33:15','frank','tapayi','system upgraded',NULL),(29,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-05 18:38:17','frank','tapayi','system upgraded',NULL),(30,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-06 12:57:39','frank','tapayi','system upgraded',NULL),(31,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-07 12:22:56','frank','tapayi','system upgraded',NULL),(32,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-07 12:32:38','frank','tapayi','system upgraded',NULL),(33,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-07 13:21:12','frank','tapayi','system upgraded',NULL),(34,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-07 13:32:17','frank','tapayi','system upgraded',NULL),(35,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-07 14:47:00','frank','tapayi','system upgraded',NULL),(36,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-07 14:51:17','frank','tapayi','system upgraded',NULL),(37,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-07 16:16:46','frank','tapayi','system upgraded',NULL),(38,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-08 14:42:10','frank','tapayi','system upgraded',NULL),(39,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-10 10:30:46','frank','tapayi','system upgraded',NULL),(40,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-10 13:21:47','frank','tapayi','system upgraded',NULL),(41,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-10 17:50:37','frank','tapayi','system upgraded',NULL),(42,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-11 16:37:02','frank','tapayi','system upgraded',NULL),(43,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-11 18:25:21','frank','tapayi','system upgraded',NULL),(44,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-12 15:31:34','frank','tapayi','system upgraded',NULL),(45,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-13 06:06:17','frank','tapayi','system upgraded',NULL),(46,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-15 11:16:23','frank','tapayi','system upgraded',NULL),(47,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 09:28:28','frank','tapayi','system upgraded',NULL),(48,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 09:47:25','frank','tapayi','system upgraded',NULL),(49,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 09:56:25','frank','tapayi','system upgraded',NULL),(50,'Created account','Naice','127.0.1.1','2019-02-16 10:20:33','frank','tapayi','system upgraded',NULL),(51,'Loged In','naice@gmail.com','127.0.1.1','2019-02-16 10:20:53','frank','tapayi','system upgraded',NULL),(52,'Loged In','naice@gmail.com','127.0.1.1','2019-02-16 10:22:52','frank','tapayi','system upgraded',NULL),(53,'Loged In','naice@gmail.com','127.0.1.1','2019-02-16 10:29:52','frank','tapayi','system upgraded',NULL),(54,'Loged In','naice@gmail.com','127.0.1.1','2019-02-16 10:38:43','frank','tapayi','system upgraded',NULL),(55,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 11:09:15','frank','tapayi','system upgraded',NULL),(56,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 11:12:05','frank','tapayi','system upgraded',NULL),(57,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 11:54:05','frank','tapayi','system upgraded',NULL),(58,'Loged In','naice@gmail.com','127.0.1.1','2019-02-16 13:33:42','frank','tapayi','system upgraded',NULL),(59,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 13:46:55','frank','tapayi','system upgraded',NULL),(60,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 14:34:17','frank','tapayi','system upgraded',NULL),(61,'Loged In','naice@gmail.com','127.0.1.1','2019-02-16 16:42:19','frank','tapayi','system upgraded',NULL),(62,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-16 17:00:12','frank','tapayi','system upgraded',NULL),(63,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-18 07:29:03','frank','tapayi','system upgraded',NULL),(64,'Loged In','juliushirwa@gmail.com','127.0.1.1','2019-02-18 16:56:45','frank','tapayi','system upgraded',NULL);
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ordes`
--

DROP TABLE IF EXISTS `ordes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ordes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `product` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `quantity` varchar(200) DEFAULT NULL,
  `in_date` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `ordes_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ordes`
--

LOCK TABLES `ordes` WRITE;
/*!40000 ALTER TABLE `ordes` DISABLE KEYS */;
/*!40000 ALTER TABLE `ordes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payments`
--

DROP TABLE IF EXISTS `payments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payments`
--

LOCK TABLES `payments` WRITE;
/*!40000 ALTER TABLE `payments` DISABLE KEYS */;
/*!40000 ALTER TABLE `payments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `post`
--

DROP TABLE IF EXISTS `post`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(80) DEFAULT NULL,
  `body` text,
  `pub_date` datetime DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `post_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `post`
--

LOCK TABLES `post` WRITE;
/*!40000 ALTER TABLE `post` DISABLE KEYS */;
/*!40000 ALTER TABLE `post` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `products` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `quantity` varchar(200) DEFAULT NULL,
  `in_date` varchar(200) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profiles`
--

DROP TABLE IF EXISTS `profiles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `profiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `primary_school` varchar(200) DEFAULT NULL,
  `secondary_school` varchar(200) DEFAULT NULL,
  `university_school` varchar(200) DEFAULT NULL,
  `vocational_school` varchar(200) DEFAULT NULL,
  `exp1` varchar(200) DEFAULT NULL,
  `exp2` varchar(200) DEFAULT NULL,
  `exp3` varchar(200) DEFAULT NULL,
  `strn1` varchar(200) DEFAULT NULL,
  `strn2` varchar(200) DEFAULT NULL,
  `strn3` varchar(200) DEFAULT NULL,
  `car1` varchar(200) DEFAULT NULL,
  `car2` varchar(200) DEFAULT NULL,
  `car3` varchar(200) DEFAULT NULL,
  `inter1` varchar(200) DEFAULT NULL,
  `inter2` varchar(200) DEFAULT NULL,
  `inter3` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `profiles_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profiles`
--

LOCK TABLES `profiles` WRITE;
/*!40000 ALTER TABLE `profiles` DISABLE KEYS */;
/*!40000 ALTER TABLE `profiles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `projects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `starting_date` varchar(200) DEFAULT NULL,
  `ending_date` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `duration` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reports`
--

DROP TABLE IF EXISTS `reports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reports` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(200) DEFAULT NULL,
  `project` varchar(200) DEFAULT NULL,
  `task` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `notes` varchar(200) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `reports_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reports`
--

LOCK TABLES `reports` WRITE;
/*!40000 ALTER TABLE `reports` DISABLE KEYS */;
/*!40000 ALTER TABLE `reports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(60) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `roles_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rukomatanyo`
--

DROP TABLE IF EXISTS `rukomatanyo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rukomatanyo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tariki_byakozwe` datetime DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `piyesi` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `rukomatanyo_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rukomatanyo`
--

LOCK TABLES `rukomatanyo` WRITE;
/*!40000 ALTER TABLE `rukomatanyo` DISABLE KEYS */;
INSERT INTO `rukomatanyo` VALUES (1,'2019-02-18 00:00:00','gufatanya guhinga','1255',NULL),(2,'2019-02-19 00:00:00','gufatanya guhinga','152',NULL),(3,'2019-02-18 00:00:00','gufatanya guhinga','2000',NULL),(4,'2019-02-18 00:00:00','gufatanya guhinga','2000',NULL),(5,'2019-02-18 00:00:00','gufatanya guhinga','1255',NULL),(6,'2019-02-19 00:00:00','gufatanya guhinga','2000',NULL),(7,'2019-02-18 00:00:00','gufatanya guhinga','152','juliushirwa@gmail.com'),(8,'2019-02-18 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(9,'2019-02-18 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(10,'2019-02-15 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(11,'2019-02-18 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(12,'2019-02-19 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(13,'2019-02-20 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(14,'2019-02-14 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(15,'2019-02-18 00:00:00','gufatanya guhinga','1255','juliushirwa@gmail.com'),(16,'2019-02-20 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(17,'2019-02-19 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(18,'2019-02-18 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(19,'2019-02-18 00:00:00','gufatanya guhinga','2000','juliushirwa@gmail.com'),(20,'2014-10-10 00:00:00','Kugura ifumbire','505',NULL),(21,'2020-11-11 00:00:00','Kuzigama','900','juliushirwa@gmail.com');
/*!40000 ALTER TABLE `rukomatanyo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `shares`
--

DROP TABLE IF EXISTS `shares`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `shares` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `memberId` varchar(200) DEFAULT NULL,
  `shareAccNo` varchar(200) DEFAULT NULL,
  `memberName` varchar(200) DEFAULT NULL,
  `depositOrWithdraw` varchar(200) DEFAULT NULL,
  `shareAmount` varchar(200) DEFAULT NULL,
  `balanceShare` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `shares`
--

LOCK TABLES `shares` WRITE;
/*!40000 ALTER TABLE `shares` DISABLE KEYS */;
/*!40000 ALTER TABLE `shares` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `staffs`
--

DROP TABLE IF EXISTS `staffs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `staffs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(60) DEFAULT NULL,
  `last_name` varchar(60) DEFAULT NULL,
  `nid` varchar(60) DEFAULT NULL,
  `district` varchar(60) DEFAULT NULL,
  `sector` varchar(60) DEFAULT NULL,
  `sex` varchar(60) DEFAULT NULL,
  `yob` varchar(60) DEFAULT NULL,
  `position` varchar(60) DEFAULT NULL,
  `education` varchar(60) DEFAULT NULL,
  `telephone` varchar(60) DEFAULT NULL,
  `email` varchar(60) DEFAULT NULL,
  `monthly_net_salary` varchar(60) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `staffs_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `staffs`
--

LOCK TABLES `staffs` WRITE;
/*!40000 ALTER TABLE `staffs` DISABLE KEYS */;
/*!40000 ALTER TABLE `staffs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trainings`
--

DROP TABLE IF EXISTS `trainings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trainings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `trainer` varchar(200) DEFAULT NULL,
  `about` varchar(200) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `trainings_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trainings`
--

LOCK TABLES `trainings` WRITE;
/*!40000 ALTER TABLE `trainings` DISABLE KEYS */;
/*!40000 ALTER TABLE `trainings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transactions`
--

DROP TABLE IF EXISTS `transactions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `transactions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bankAccountNumber` varchar(200) DEFAULT NULL,
  `memberName` varchar(200) DEFAULT NULL,
  `accountType` varchar(200) DEFAULT NULL,
  `depositOrWithdraw` varchar(200) DEFAULT NULL,
  `cashOrCheque` varchar(200) DEFAULT NULL,
  `amount` varchar(200) DEFAULT NULL,
  `balance` varchar(200) DEFAULT NULL,
  `date` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transactions`
--

LOCK TABLES `transactions` WRITE;
/*!40000 ALTER TABLE `transactions` DISABLE KEYS */;
/*!40000 ALTER TABLE `transactions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ububiko`
--

DROP TABLE IF EXISTS `ububiko`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ububiko` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `ububiko_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `ububiko_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ububiko`
--

LOCK TABLES `ububiko` WRITE;
/*!40000 ALTER TABLE `ububiko` DISABLE KEYS */;
INSERT INTO `ububiko` VALUES (1,5,4,NULL,'2019-02-03 14:02:00','juliushirwa@gmail.com',NULL),(2,7,5,NULL,'2019-02-03 14:04:20','juliushirwa@gmail.com',NULL),(3,5,4,NULL,'2019-02-03 14:15:57','juliushirwa@gmail.com',NULL),(4,400000,500000,NULL,'2019-02-18 10:28:01','juliushirwa@gmail.com',11);
/*!40000 ALTER TABLE `ububiko` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubugenzuzi`
--

DROP TABLE IF EXISTS `ubugenzuzi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ubugenzuzi` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(200) DEFAULT NULL,
  `decision` varchar(200) DEFAULT NULL,
  `owner` varchar(200) DEFAULT NULL,
  `stakeholders` varchar(200) DEFAULT NULL,
  `due_date` varchar(200) DEFAULT NULL,
  `background` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `ubugenzuzi_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubugenzuzi`
--

LOCK TABLES `ubugenzuzi` WRITE;
/*!40000 ALTER TABLE `ubugenzuzi` DISABLE KEYS */;
/*!40000 ALTER TABLE `ubugenzuzi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `umugabaneShingiro`
--

DROP TABLE IF EXISTS `umugabaneShingiro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `umugabaneShingiro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ayinjiye` int(11) DEFAULT NULL,
  `ayasohotse` int(11) DEFAULT NULL,
  `asigaye` int(11) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `umugabaneShingiro_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `umugabaneShingiro_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umugabaneShingiro`
--

LOCK TABLES `umugabaneShingiro` WRITE;
/*!40000 ALTER TABLE `umugabaneShingiro` DISABLE KEYS */;
INSERT INTO `umugabaneShingiro` VALUES (1,8,4,NULL,'2019-02-03 14:20:07','juliushirwa@gmail.com',NULL),(2,5,4,NULL,'2019-02-03 15:16:17','juliushirwa@gmail.com',NULL),(3,10,1000,NULL,'2019-02-18 10:34:37','juliushirwa@gmail.com',12);
/*!40000 ALTER TABLE `umugabaneShingiro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `umusanzu`
--

DROP TABLE IF EXISTS `umusanzu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `umusanzu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `UmusoroWakarere` int(11) DEFAULT NULL,
  `UmusanzuCoop` int(11) DEFAULT NULL,
  `Umugabane` int(11) DEFAULT NULL,
  `Ikigega` int(11) DEFAULT NULL,
  `KuzibaIcyuho` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `umusanzu_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `umusanzu_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umusanzu`
--

LOCK TABLES `umusanzu` WRITE;
/*!40000 ALTER TABLE `umusanzu` DISABLE KEYS */;
INSERT INTO `umusanzu` VALUES (1,5164,3990,0,500,8200,96,'2019-02-16 11:42:22','juliushirwa@gmail.com'),(2,5146,3990,0,500,8200,96,'2019-02-16 12:03:26','juliushirwa@gmail.com'),(3,0,0,0,0,0,138,'2019-02-16 13:51:00','juliushirwa@gmail.com');
/*!40000 ALTER TABLE `umusanzu` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `umusaruro`
--

DROP TABLE IF EXISTS `umusaruro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `umusaruro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amazina` varchar(100) DEFAULT NULL,
  `resi` int(11) DEFAULT NULL,
  `zone` varchar(100) DEFAULT NULL,
  `group` varchar(100) DEFAULT NULL,
  `umusaruro` int(11) DEFAULT NULL,
  `umuceriYagurijwe` int(11) DEFAULT NULL,
  `umuceriWoKurya` int(11) DEFAULT NULL,
  `umuceriWoKugurisha` int(11) DEFAULT NULL,
  `igiciroCyaKimwe` int(11) DEFAULT NULL,
  `umusanzu` int(11) DEFAULT NULL,
  `amafarangaYose` int(11) DEFAULT NULL,
  `amafarangaYoGutonoza` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `umwakaWisarura` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `umusaruro_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `umusaruro_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umusaruro`
--

LOCK TABLES `umusaruro` WRITE;
/*!40000 ALTER TABLE `umusaruro` DISABLE KEYS */;
/*!40000 ALTER TABLE `umusaruro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `umusarurob`
--

DROP TABLE IF EXISTS `umusarurob`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `umusarurob` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `RiceType` varchar(100) DEFAULT NULL,
  `RiceAmount` int(11) DEFAULT NULL,
  `UwoAsigaranye` int(11) DEFAULT NULL,
  `UwoKugurisha` int(11) DEFAULT NULL,
  `GutonozaAmount` int(11) DEFAULT NULL,
  `AmafarangaUmusaruro1` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `umusarurob_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `umusarurob_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umusarurob`
--

LOCK TABLES `umusarurob` WRITE;
/*!40000 ALTER TABLE `umusarurob` DISABLE KEYS */;
INSERT INTO `umusarurob` VALUES (16,'Umusaruro short',6785,0,23,0,6785,338,'naice@gmail.com','2019-02-16 11:06:09'),(17,'Umusaruro long',81130,0,266,0,81130,276,'naice@gmail.com','2019-02-16 11:07:10'),(18,'Umusaruro short',247210,0,838,0,247210,138,'juliushirwa@gmail.com','2019-02-16 11:12:10'),(19,'Umusaruro long',81130,0,266,0,81130,96,'juliushirwa@gmail.com','2019-02-16 11:15:27'),(20,'Umusaruro short',10325,0,35,0,10325,139,'juliushirwa@gmail.com','2019-02-16 11:30:09');
/*!40000 ALTER TABLE `umusarurob` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `unions`
--

DROP TABLE IF EXISTS `unions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `unions` (
  `id` int(11) DEFAULT NULL,
  `sno` varchar(200) DEFAULT NULL,
  `code` varchar(200) DEFAULT NULL,
  `name` varchar(200) DEFAULT NULL,
  `certificate` varchar(200) DEFAULT NULL,
  `reg_date` varchar(200) DEFAULT NULL,
  `province` varchar(200) DEFAULT NULL,
  `district` varchar(200) DEFAULT NULL,
  `sector` varchar(200) DEFAULT NULL,
  `activity` varchar(200) DEFAULT NULL,
  `federation_id` int(11) DEFAULT NULL,
  `email` varchar(200) NOT NULL,
  PRIMARY KEY (`email`),
  KEY `federation_id` (`federation_id`),
  CONSTRAINT `unions_ibfk_1` FOREIGN KEY (`federation_id`) REFERENCES `federations` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `unions`
--

LOCK TABLES `unions` WRITE;
/*!40000 ALTER TABLE `unions` DISABLE KEYS */;
/*!40000 ALTER TABLE `unions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(200) DEFAULT NULL,
  `secondname` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `zones`
--

DROP TABLE IF EXISTS `zones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `zones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `izina` varchar(100) DEFAULT NULL,
  `ubusobanuro` varchar(200) DEFAULT NULL,
  `impamvu` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `rukomatanyo_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `rukomatanyo_id` (`rukomatanyo_id`),
  CONSTRAINT `zones_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `zones_ibfk_2` FOREIGN KEY (`rukomatanyo_id`) REFERENCES `rukomatanyo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zones`
--

LOCK TABLES `zones` WRITE;
/*!40000 ALTER TABLE `zones` DISABLE KEYS */;
INSERT INTO `zones` VALUES (1,'Bugesera','zone ya bugesera','gufatanya guhinga','juliushirwa@gmail.com',NULL);
/*!40000 ALTER TABLE `zones` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-18 19:11:46
