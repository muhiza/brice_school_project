-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: aicos
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Assets`
--

LOCK TABLES `Assets` WRITE;
/*!40000 ALTER TABLE `Assets` DISABLE KEYS */;
/*!40000 ALTER TABLE `Assets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `CRMs`
--

DROP TABLE IF EXISTS `CRMs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `CRMs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` varchar(200) DEFAULT NULL,
  `tag` varchar(100) DEFAULT NULL,
  `company_name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `address` varchar(200) DEFAULT NULL,
  `contact_type` varchar(200) DEFAULT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `CRMs_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `CRMs_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `CRMs`
--

LOCK TABLES `CRMs` WRITE;
/*!40000 ALTER TABLE `CRMs` DISABLE KEYS */;
/*!40000 ALTER TABLE `CRMs` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `InguzanyoZatanzwe`
--

LOCK TABLES `InguzanyoZatanzwe` WRITE;
/*!40000 ALTER TABLE `InguzanyoZatanzwe` DISABLE KEYS */;
/*!40000 ALTER TABLE `InguzanyoZatanzwe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `abishyuwe`
--

DROP TABLE IF EXISTS `abishyuwe`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `abishyuwe` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount_payed` int(11) DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `member_name` varchar(200) DEFAULT NULL,
  `ibiro` float DEFAULT NULL,
  `done_date` date DEFAULT NULL,
  `umusaruro_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  KEY `umusaruro_id` (`umusaruro_id`),
  CONSTRAINT `abishyuwe_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `abishyuwe_ibfk_2` FOREIGN KEY (`umusaruro_id`) REFERENCES `umusarurob` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `abishyuwe`
--

LOCK TABLES `abishyuwe` WRITE;
/*!40000 ALTER TABLE `abishyuwe` DISABLE KEYS */;
/*!40000 ALTER TABLE `abishyuwe` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `account`
--

DROP TABLE IF EXISTS `account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AccountName` varchar(200) DEFAULT NULL,
  `Description` varchar(200) DEFAULT NULL,
  `cooperative_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  CONSTRAINT `account_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('91cc4df90599');
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amatsinda`
--

LOCK TABLES `amatsinda` WRITE;
/*!40000 ALTER TABLE `amatsinda` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `applytrainings`
--

LOCK TABLES `applytrainings` WRITE;
/*!40000 ALTER TABLE `applytrainings` DISABLE KEYS */;
/*!40000 ALTER TABLE `applytrainings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `assetsaccounting`
--

DROP TABLE IF EXISTS `assetsaccounting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `assetsaccounting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Date` varchar(200) DEFAULT NULL,
  `Category` varchar(200) DEFAULT NULL,
  `Account` varchar(200) DEFAULT NULL,
  `Amount` varchar(200) DEFAULT NULL,
  `Description` varchar(200) DEFAULT NULL,
  `cooperative_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  CONSTRAINT `assetsaccounting_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assetsaccounting`
--

LOCK TABLES `assetsaccounting` WRITE;
/*!40000 ALTER TABLE `assetsaccounting` DISABLE KEYS */;
/*!40000 ALTER TABLE `assetsaccounting` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bank`
--

LOCK TABLES `bank` WRITE;
/*!40000 ALTER TABLE `bank` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bankaccounts`
--

LOCK TABLES `bankaccounts` WRITE;
/*!40000 ALTER TABLE `bankaccounts` DISABLE KEYS */;
/*!40000 ALTER TABLE `bankaccounts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `budget`
--

DROP TABLE IF EXISTS `budget`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `budget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Category` varchar(200) DEFAULT NULL,
  `Date` varchar(200) DEFAULT NULL,
  `Amount` varchar(200) DEFAULT NULL,
  `cooperative_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  CONSTRAINT `budget_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `budget`
--

LOCK TABLES `budget` WRITE;
/*!40000 ALTER TABLE `budget` DISABLE KEYS */;
/*!40000 ALTER TABLE `budget` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `coopMemberBankAccounts`
--

LOCK TABLES `coopMemberBankAccounts` WRITE;
/*!40000 ALTER TABLE `coopMemberBankAccounts` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (NULL,NULL,NULL,'mamy@gmail.com','CORIKA',NULL,NULL,NULL,'Kigali City','Gasabo','Gatsata','Karuruma','Rice',NULL,NULL,NULL,'2019-10-18 03:34:46','200000','20000','40','60',1);
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
  `is_manager` tinyint(1) DEFAULT NULL,
  `is_accountant` tinyint(1) DEFAULT NULL,
  `is_production_manager` tinyint(1) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'mamy@gmail.com','mamy',NULL,NULL,'+250787104701','pbkdf2:sha256:150000$0d7ebK62$62ac0060c50ac3bbc349b5731405f258f6bc6e33c0dbae825644f40f82e41374',NULL,NULL,NULL,NULL,NULL,1,1,0,0,0,0,0,0,0,0,0,NULL,NULL);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense`
--

DROP TABLE IF EXISTS `expense`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `expense` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(200) DEFAULT NULL,
  `Date` varchar(200) DEFAULT NULL,
  `Category` varchar(200) DEFAULT NULL,
  `Account` varchar(200) DEFAULT NULL,
  `Amount` varchar(200) DEFAULT NULL,
  `Desciption` varchar(200) DEFAULT NULL,
  `cooperative_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  CONSTRAINT `expense_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense`
--

LOCK TABLES `expense` WRITE;
/*!40000 ALTER TABLE `expense` DISABLE KEYS */;
/*!40000 ALTER TABLE `expense` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expensecategory`
--

DROP TABLE IF EXISTS `expensecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `expensecategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AccountName` varchar(200) DEFAULT NULL,
  `cooperative_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  CONSTRAINT `expensecategory_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expensecategory`
--

LOCK TABLES `expensecategory` WRITE;
/*!40000 ALTER TABLE `expensecategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `expensecategory` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibicuruzwa`
--

LOCK TABLES `ibicuruzwa` WRITE;
/*!40000 ALTER TABLE `ibicuruzwa` DISABLE KEYS */;
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
  `AmandeC` varchar(200) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibihano`
--

LOCK TABLES `ibihano` WRITE;
/*!40000 ALTER TABLE `ibihano` DISABLE KEYS */;
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
  `UmuceriGrade` varchar(200) DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibindi`
--

LOCK TABLES `ibindi` WRITE;
/*!40000 ALTER TABLE `ibindi` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibindiRukomatanya`
--

LOCK TABLES `ibindiRukomatanya` WRITE;
/*!40000 ALTER TABLE `ibindiRukomatanya` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibiramba`
--

LOCK TABLES `ibiramba` WRITE;
/*!40000 ALTER TABLE `ibiramba` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ibirarane`
--

LOCK TABLES `ibirarane` WRITE;
/*!40000 ALTER TABLE `ibirarane` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ikoreshwaRyimari`
--

LOCK TABLES `ikoreshwaRyimari` WRITE;
/*!40000 ALTER TABLE `ikoreshwaRyimari` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inamaubuyobozi`
--

LOCK TABLES `inamaubuyobozi` WRITE;
/*!40000 ALTER TABLE `inamaubuyobozi` DISABLE KEYS */;
/*!40000 ALTER TABLE `inamaubuyobozi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `income`
--

DROP TABLE IF EXISTS `income`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `income` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(200) DEFAULT NULL,
  `Date` varchar(200) DEFAULT NULL,
  `Category` varchar(200) DEFAULT NULL,
  `Account` varchar(200) DEFAULT NULL,
  `Amount` varchar(200) DEFAULT NULL,
  `Desciption` varchar(200) DEFAULT NULL,
  `cooperative_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  CONSTRAINT `income_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `income`
--

LOCK TABLES `income` WRITE;
/*!40000 ALTER TABLE `income` DISABLE KEYS */;
/*!40000 ALTER TABLE `income` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `incomecategory`
--

DROP TABLE IF EXISTS `incomecategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `incomecategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `Category` varchar(200) DEFAULT NULL,
  `cooperative_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `cooperative_id` (`cooperative_id`),
  CONSTRAINT `incomecategory_ibfk_1` FOREIGN KEY (`cooperative_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `incomecategory`
--

LOCK TABLES `incomecategory` WRITE;
/*!40000 ALTER TABLE `incomecategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `incomecategory` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inguzanyozabandi`
--

LOCK TABLES `inguzanyozabandi` WRITE;
/*!40000 ALTER TABLE `inguzanyozabandi` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inkunga`
--

LOCK TABLES `inkunga` WRITE;
/*!40000 ALTER TABLE `inkunga` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inyongeramusaruro`
--

LOCK TABLES `inyongeramusaruro` WRITE;
/*!40000 ALTER TABLE `inyongeramusaruro` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `isandukunshya`
--

LOCK TABLES `isandukunshya` WRITE;
/*!40000 ALTER TABLE `isandukunshya` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `members`
--

LOCK TABLES `members` WRITE;
/*!40000 ALTER TABLE `members` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
INSERT INTO `notifications` VALUES (1,'Created account','mamy','127.0.1.1','2019-10-18 03:33:50','frank','tapayi','system upgraded',NULL),(2,'Loged In','mamy@gmail.com','127.0.1.1','2019-10-18 03:34:03','frank','tapayi','system upgraded',NULL),(3,'Loged In','mamy@gmail.com','127.0.1.1','2019-10-18 03:35:00','frank','tapayi','system upgraded',NULL);
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `tariki_byakozwe` date DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  `piyesi` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `rukomatanyo_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rukomatanyo`
--

LOCK TABLES `rukomatanyo` WRITE;
/*!40000 ALTER TABLE `rukomatanyo` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ububiko`
--

LOCK TABLES `ububiko` WRITE;
/*!40000 ALTER TABLE `ububiko` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubugenzuzi`
--

LOCK TABLES `ubugenzuzi` WRITE;
/*!40000 ALTER TABLE `ubugenzuzi` DISABLE KEYS */;
/*!40000 ALTER TABLE `ubugenzuzi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubwisazures`
--

DROP TABLE IF EXISTS `ubwisazures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ubwisazures` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `AssetDescription` varchar(200) DEFAULT NULL,
  `cost` int(11) DEFAULT NULL,
  `YearOfPurchase` varchar(200) DEFAULT NULL,
  `SalvageValue` int(11) DEFAULT NULL,
  `UsefulLife` varchar(200) DEFAULT NULL,
  `Method` varchar(200) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  KEY `department_id` (`department_id`),
  CONSTRAINT `ubwisazures_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubwisazures`
--

LOCK TABLES `ubwisazures` WRITE;
/*!40000 ALTER TABLE `ubwisazures` DISABLE KEYS */;
/*!40000 ALTER TABLE `ubwisazures` ENABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umugabaneShingiro`
--

LOCK TABLES `umugabaneShingiro` WRITE;
/*!40000 ALTER TABLE `umugabaneShingiro` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umusanzu`
--

LOCK TABLES `umusanzu` WRITE;
/*!40000 ALTER TABLE `umusanzu` DISABLE KEYS */;
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
  `umuceriWoKurya` float DEFAULT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
  `UmusaruroGrade` int(11) DEFAULT NULL,
  `RiceAmount` int(11) DEFAULT NULL,
  `UwoAsigaranye` float DEFAULT NULL,
  `UwoKugurisha` int(11) DEFAULT NULL,
  `GutonozaAmount` int(11) DEFAULT NULL,
  `AmafarangaUmusaruro1` int(11) DEFAULT NULL,
  `Asigaye` float DEFAULT NULL,
  `member_id` int(11) DEFAULT NULL,
  `department_id` varchar(200) DEFAULT NULL,
  `done_date` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `department_id` (`department_id`),
  KEY `member_id` (`member_id`),
  CONSTRAINT `umusarurob_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`email`),
  CONSTRAINT `umusarurob_ibfk_2` FOREIGN KEY (`member_id`) REFERENCES `members` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `umusarurob`
--

LOCK TABLES `umusarurob` WRITE;
/*!40000 ALTER TABLE `umusarurob` DISABLE KEYS */;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `zones`
--

LOCK TABLES `zones` WRITE;
/*!40000 ALTER TABLE `zones` DISABLE KEYS */;
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

-- Dump completed on 2019-10-18  7:29:22
