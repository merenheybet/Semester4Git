CREATE DATABASE  IF NOT EXISTS `Versicherung` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `Versicherung`;

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

--
-- Table structure for table `Abteilung`
--

DROP TABLE IF EXISTS `Abteilung`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Abteilung` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Bezeichnung` varchar(30) NOT NULL,
  `Ort` varchar(30) DEFAULT NULL,
  `Kuerzel` char(4) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Abteilung`
--

LOCK TABLES `Abteilung` WRITE;
/*!40000 ALTER TABLE `Abteilung` DISABLE KEYS */;
INSERT INTO `Abteilung` VALUES (1,'Finanzbuchhaltung','Dortmund','Fibu'),(2,'Anlagenbuchhaltung','Dortmund','Albu'),(3,'Kostenrechnung','Dortmund','Kore'),(4,'Kostenplanung','Dortmund','Kopl'),(5,'Vertrieb','Essen','Vert'),(6,'Lagerhaltung','Bochum','Lagh'),(7,'Produktion','Bochum','Prod'),(8,'Schadensabwicklung','Essen','ScAb'),(9,'Personalverwaltung','Essen','Pers'),(10,'Sozialverwaltung','Essen','Soz'),(11,'Ausbildung','Herne','Ausb'),(12,'Forschung und Entwicklung','Bochum','Fue');
/*!40000 ALTER TABLE `Abteilung` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Dienstwagen`
--

DROP TABLE IF EXISTS `Dienstwagen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Dienstwagen` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Kennzeichen` varchar(10) NOT NULL,
  `Farbe` varchar(30) DEFAULT NULL,
  `Fahrzeugtyp_ID` int NOT NULL,
  `Mitarbeiter_ID` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Dienstwagen_Kennzeichen` (`Kennzeichen`),
  KEY `Dienstwagen_FZ` (`Fahrzeugtyp_ID`),
  KEY `Dienstwagen_MI` (`Mitarbeiter_ID`),
  CONSTRAINT `Dienstwagen_FZ` FOREIGN KEY (`Fahrzeugtyp_ID`) REFERENCES `Fahrzeugtyp` (`ID`),
  CONSTRAINT `Dienstwagen_MI` FOREIGN KEY (`Mitarbeiter_ID`) REFERENCES `Mitarbeiter` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Dienstwagen`
--

LOCK TABLES `Dienstwagen` WRITE;
/*!40000 ALTER TABLE `Dienstwagen` DISABLE KEYS */;
INSERT INTO `Dienstwagen` VALUES (1,'DO-WB 421','elfenbein',14,1),(2,'DO-WB 422','elfenbein',14,3),(3,'DO-WB 423','elfenbein',14,5),(4,'DO-WB 424','elfenbein',14,7),(5,'DO-WB 425','elfenbein',14,9),(6,'DO-WB 426','elfenbein',14,13),(7,'DO-WB 427','elfenbein',14,15),(8,'DO-WB 428','elfenbein',14,17),(9,'DO-WB 429','elfenbein',14,21),(10,'DO-WB 4210','elfenbein',14,23),(11,'DO-WB 4211','elfenbein',14,25),(12,'DO-WB 4212','elfenbein',14,27),(16,'DO-WB 111','elfenbein',16,NULL),(17,'DO-WB 352','gelb',2,10),(18,'DO-WB 353','gelb',3,11),(19,'DO-WB 354','gelb',4,12),(20,'DO-WB 382','gelb',2,18),(21,'DO-WB 383','gelb',3,19),(22,'DO-WB 384','gelb',4,20);
/*!40000 ALTER TABLE `Dienstwagen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Fahrzeug`
--

DROP TABLE IF EXISTS `Fahrzeug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Fahrzeug` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Kennzeichen` varchar(10) NOT NULL,
  `Farbe` varchar(30) DEFAULT NULL,
  `Fahrzeugtyp_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Fahrzeug_Kennzeichen` (`Kennzeichen`),
  KEY `Fahrzeug_FK` (`Fahrzeugtyp_ID`),
  CONSTRAINT `Fahrzeug_FK` FOREIGN KEY (`Fahrzeugtyp_ID`) REFERENCES `Fahrzeugtyp` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Fahrzeug`
--

LOCK TABLES `Fahrzeug` WRITE;
/*!40000 ALTER TABLE `Fahrzeug` DISABLE KEYS */;
INSERT INTO `Fahrzeug` VALUES (1,'RE-LM 901','ocker',5),(2,'RE-LM 902','ocker',5),(3,'RE-LM 903','ocker',5),(4,'GE-AB 123','schwarz',22),(5,'RE-CD 456','ocker',21),(6,'HER-EF 789','gelb',20),(7,'BO-GH 102','rot',19),(8,'E-IJ 345','bordeaux',18),(9,'BO-KL 678','blau',17),(10,'RE-MN 901','elfenbein',16),(11,'RE-OP 234','ocker',15),(12,'RE-QR 567','gelb',14),(13,'RE-ST 890','rot',13),(14,'RE-UV 135','bordeaux',12),(15,'RE-WX 791','ocker',11),(16,'RE-YZ 369','rot',10),(17,'GE-AC 246','elfenbein',9),(18,'GE-EG 892','blau',8),(19,'OB-FH 470','elfenbein',7),(20,'BOT-KI 357','rot',6),(21,'BOR-NO 234','gelb',4),(22,'BOR-PQ 567','elfenbein',3),(23,'BOR-RS 890','gelb',2),(24,'K-XR 147',NULL,6),(25,'HH-MM 783','schwarz',7);
/*!40000 ALTER TABLE `Fahrzeug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Fahrzeughersteller`
--

DROP TABLE IF EXISTS `Fahrzeughersteller`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Fahrzeughersteller` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Land` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Fahrzeughersteller`
--

LOCK TABLES `Fahrzeughersteller` WRITE;
/*!40000 ALTER TABLE `Fahrzeughersteller` DISABLE KEYS */;
INSERT INTO `Fahrzeughersteller` VALUES (1,'Volkswagen','Deutschland'),(2,'Opel','Deutschland'),(3,'Ford','Deutschland'),(4,'BMW','Deutschland'),(5,'Audi','Deutschland'),(6,'Mercedes-Benz','Deutschland'),(7,'Sachsenring','Deutschland'),(8,'Saab','Schweden'),(9,'Volvo',NULL),(10,'Renault','Frankreich'),(11,'Seat',NULL);
/*!40000 ALTER TABLE `Fahrzeughersteller` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Fahrzeugtyp`
--

DROP TABLE IF EXISTS `Fahrzeugtyp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Fahrzeugtyp` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Bezeichnung` varchar(30) NOT NULL,
  `Hersteller_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Fahrzeugtyp_FK` (`Hersteller_ID`),
  CONSTRAINT `Fahrzeugtyp_FK` FOREIGN KEY (`Hersteller_ID`) REFERENCES `Fahrzeughersteller` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Fahrzeugtyp`
--

LOCK TABLES `Fahrzeugtyp` WRITE;
/*!40000 ALTER TABLE `Fahrzeugtyp` DISABLE KEYS */;
INSERT INTO `Fahrzeugtyp` VALUES (1,'Polo',1),(2,'Golf',1),(3,'Passat',1),(4,'Kadett',2),(5,'Corsa',2),(6,'Focus',3),(7,'Trabant',7),(8,'Fiesta',3),(9,'325',4),(10,'525',4),(11,'Z3',4),(12,'A3',5),(13,'A4',5),(14,'A160',6),(15,'W204 (C-Klasse)',6),(16,'W211 (E-Klasse)',6),(17,'Saab 9-3',8),(18,'S40',9),(19,'C30',9),(20,'Clio',10),(21,'Twingo',10),(22,'Ibiza',11),(23,'Leon',11);
/*!40000 ALTER TABLE `Fahrzeugtyp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Mitarbeiter`
--

DROP TABLE IF EXISTS `Mitarbeiter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Mitarbeiter` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Personalnummer` varchar(10) NOT NULL,
  `Name` varchar(30) NOT NULL,
  `Vorname` varchar(30) NOT NULL,
  `Geburtsdatum` date NOT NULL,
  `Telefon` varchar(30) DEFAULT NULL,
  `Mobil` varchar(30) DEFAULT NULL,
  `Email` varchar(50) DEFAULT NULL,
  `Raum` varchar(10) DEFAULT NULL,
  `Ist_Leiter` char(1) NOT NULL DEFAULT 'N',
  `Abteilung_ID` int NOT NULL,
  `Geschlecht` char(1) NOT NULL DEFAULT 'W',
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Mitarbeiter_Nummer` (`Personalnummer`),
  KEY `Mitarbeiter_Name` (`Name`,`Vorname`),
  KEY `Mitarbeiter_FK` (`Abteilung_ID`),
  CONSTRAINT `Mitarbeiter_FK` FOREIGN KEY (`Abteilung_ID`) REFERENCES `Abteilung` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Mitarbeiter`
--

LOCK TABLES `Mitarbeiter` WRITE;
/*!40000 ALTER TABLE `Mitarbeiter` DISABLE KEYS */;
INSERT INTO `Mitarbeiter` VALUES (1,'10001','Müller','Kurt','1977-01-05','0231/5554987','','kurt.mueller@unserefirma.de','112','J',1,'M'),(2,'10002','Schneider','Daniela','1980-02-16','0231/5554988',NULL,'daniela.schneider@unserefirma.de','113','N',1,'W'),(3,'20001','Meyer','Walter','1963-07-02','0231/5553967','','walter.meyer@unserefirma.de','212','J',2,'M'),(4,'20002','Schmitz','Michael','1959-08-25','0231/5556187',NULL,'michael.schmitz@unserefirma.de','212','N',2,'M'),(5,'30001','Wagner','Gaby','1970-01-18','0231/5554787','','gaby.wagner@unserefirma.de','312','J',3,'W'),(6,'30002','Feyerabend','Werner','1982-04-01','0231/5554997',NULL,'werner.feyerabend@unserefirma.de','316','N',3,'M'),(7,'40001','Langmann','Matthias','1976-03-28','0231/5551927','','matthias.langmann@unserefirma.de','412','J',4,'M'),(8,'40002','Peters','Michael','1973-11-15','0231/5554237',NULL,'michael.peters@unserefirma.de','412','N',4,'M'),(9,'50001','Pohl','Helmut','1980-10-27','0201/4014186','(0171) 4123456','helmut.pohl@unserefirma.de','152','J',5,'M'),(10,'50002','Braun','Christian','1966-09-05','0201/4014726','(0170) 8351647','christian.braun@unserefirma.de','153','N',5,'M'),(11,'50003','Polovic','Frantisek','1961-11-26','0201/4014727','(0161) 5124793','frantisek.polovic@unserefirma.de','154','N',5,'M'),(12,'50004','Kalman','Aydin','1976-12-17','0201/4014728','(0161) 4486319','aydin.kalman@unserefirma.de','155','N',5,'M'),(13,'60001','Aagenau','Karolin','1950-01-02','0234/66006001','','Karolin.Aagenau@unserefirma.de','48','J',6,'W'),(14,'60002','Pinkart','Petra','1953-03-04','0234/66006002',NULL,'Petra.Pinkart@unserefirma.de','43','N',6,'W'),(15,'70001','Olschewski','Pjotr','1956-05-06','0234/66007001','','Pjotr.Olschewski@unserefirma.de','28','J',7,'M'),(16,'70002','Nordmann','Jörg','1959-07-08','0234/66007002',NULL,'Joerg.Nordmann@unserefirma.de','27','N',7,'M'),(17,'80001','Schindler','Christina','1962-09-10','0201/4012151','(0173) 7513901','Christina.Schindler@unserefirma.de','101','J',8,'W'),(18,'80002','Aliman','Zafer','1965-11-12','0201/4012161','(0171) 9416755','Zafer.Aliman@unserefirma.de','102','N',8,'M'),(19,'80003','Langer','Norbert','1968-01-13','0201/4012171','(0162) 1357902','Norbert.Langer@unserefirma.de','103','N',8,'M'),(20,'80004','Kolic','Ivana','1971-02-14','0201/4012181','(0172) 4680135','Ivana.Kolic@unserefirma.de','104','N',8,'W'),(21,'90001','Janssen','Bernhard','1974-03-15','0201/4013111','','Bernhard.Janssen@unserefirma.de','201','J',9,'M'),(22,'90002','Hinkel','Martina','1977-04-16','0201/4013110',NULL,'Martina.Hinkel@unserefirma.de','203','N',9,'W'),(23,'100001','Grosser','Horst','1980-05-17','0201/4013344','','Horst.Grosser@unserefirma.de','271','J',10,'M'),(24,'100002','Friedrichsen','Angelina','1983-06-20','0201/4013345',NULL,'Angelina.Friedrichsen@unserefirma.de','273','N',10,'W'),(25,'110001','Eggert','Louis','1986-07-23','02323/381456','','Louis.Eggert@unserefirma.de','14','J',11,'M'),(26,'110002','Deiters','Gisela','1989-08-26','02323/381457',NULL,'Gisela.Deiters@unserefirma.de','18','N',11,'W'),(27,'120001','Carlsen','Zacharias','1965-09-29','0234/66012001','','Zacharias.Carlsen@unserefirma.de','61','J',12,'M'),(28,'120002','Baber','Yvonne','1957-10-02','0234/66012002',NULL,'Yvonne.Baber@unserefirma.de','62','N',12,'W');
/*!40000 ALTER TABLE `Mitarbeiter` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Schadensfall`
--

DROP TABLE IF EXISTS `Schadensfall`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Schadensfall` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Datum` date NOT NULL,
  `Ort` varchar(200) NOT NULL,
  `Beschreibung` varchar(1000) NOT NULL,
  `Schadenshoehe` decimal(16,2) DEFAULT NULL,
  `Verletzte` char(1) NOT NULL,
  `Mitarbeiter_ID` int NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `Schadensfall_Datum` (`Datum`),
  KEY `Schadensfall_FK` (`Mitarbeiter_ID`),
  CONSTRAINT `Schadensfall_FK` FOREIGN KEY (`Mitarbeiter_ID`) REFERENCES `Mitarbeiter` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Schadensfall`
--

LOCK TABLES `Schadensfall` WRITE;
/*!40000 ALTER TABLE `Schadensfall` DISABLE KEYS */;
INSERT INTO `Schadensfall` VALUES (1,'2007-02-03','Recklinghausen, Bergknappenstr. 144','Gartenzaun gestreift',1234.50,'N',14),(2,'2007-07-11','Haltern, Hauptstr. 46','beim Ausparken hat BO-GH 102 die Vorfahrt von RE-CD 456 missachtet',2066.00,'N',15),(3,'2007-12-19','Marl, Rathausstr./Halterner Allee','beim Abbiegen nach links hat ein fremder Wagen die Vorfahrt missachtet',3715.60,'J',14),(4,'2008-05-27','Recklinghausen, Südgrabenstr. 23','Fremdes parkendes Auto gestreift',1438.75,'N',16),(5,'2008-10-05','Dorsten, Oberhausener Str. 18','beim Ausparken hat ein fremder Wagen die Vorfahrt missachtet',1983.00,'N',14),(6,'2009-03-13','Marl, Rathausstr./Halterner Allee','beim Abbiegen nach links hat ein fremder Wagen die Vorfahrt missachtet',4092.15,'J',15),(7,'2009-08-21','Recklinghausen, Bergknappenstr. 144','Laternenpfahl umgefahren',865.00,'N',14),(8,'2009-08-01','L318 Hamm-Flaesheim','Wildunfall mit Reh; 10% Wertverlust',2471.50,'N',16);
/*!40000 ALTER TABLE `Schadensfall` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Versicherungsgesellschaft`
--

DROP TABLE IF EXISTS `Versicherungsgesellschaft`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Versicherungsgesellschaft` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Bezeichnung` varchar(30) NOT NULL,
  `Ort` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Versicherungsgesellschaft`
--

LOCK TABLES `Versicherungsgesellschaft` WRITE;
/*!40000 ALTER TABLE `Versicherungsgesellschaft` DISABLE KEYS */;
INSERT INTO `Versicherungsgesellschaft` VALUES (1,'Deutsches Kontor','Frankfurt a.M.'),(2,'Rheinischer Vers.-Verein','Oberhausen'),(3,'Knappschaftshilfe','Essen'),(4,'Hannoversche Gesellschaft','Lehrte'),(5,'Westfalen-Bruderhilfe','Recklinghausen');
/*!40000 ALTER TABLE `Versicherungsgesellschaft` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Versicherungsnehmer`
--

DROP TABLE IF EXISTS `Versicherungsnehmer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Versicherungsnehmer` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(30) NOT NULL,
  `Vorname` varchar(30) DEFAULT NULL,
  `Geburtsdatum` date DEFAULT NULL,
  `Fuehrerschein` date DEFAULT NULL,
  `Ort` varchar(30) NOT NULL,
  `PLZ` char(5) NOT NULL,
  `Strasse` varchar(30) NOT NULL,
  `Hausnummer` varchar(10) NOT NULL,
  `Eigener_Kunde` char(1) NOT NULL,
  `Versicherungsgesellschaft_ID` int DEFAULT NULL,
  `Geschlecht` char(1) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Versicherungsnehmer_Name` (`Name`,`Vorname`),
  KEY `Versicherungsnehmer_PLZ` (`PLZ`,`Ort`),
  KEY `Versicherungsgesellschaft_ID_idx` (`Versicherungsgesellschaft_ID`),
  CONSTRAINT `Versicherungsgesellschaft_ID` FOREIGN KEY (`Versicherungsgesellschaft_ID`) REFERENCES `Versicherungsgesellschaft` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Versicherungsnehmer`
--

LOCK TABLES `Versicherungsnehmer` WRITE;
/*!40000 ALTER TABLE `Versicherungsnehmer` DISABLE KEYS */;
INSERT INTO `Versicherungsnehmer` VALUES (1,'Heckel Obsthandel GmbH','',NULL,NULL,'Dorsten','46282','Gahlener Str.','40','J',NULL,NULL),(2,'Antonius','Bernhard','1950-02-01','1972-04-03','Gelsenkirchen','45892','Coesfelder Str.','23','J',NULL,'M'),(3,'Cornelsen','Dorothea','1951-06-05','1974-08-07','Castrop-Rauxel','44577','Kiefernweg','9','J',NULL,NULL),(4,'Elberfeld','Fritz','1952-10-09','1976-12-11','Herne','44625','Haberstr.','13','J',NULL,'M'),(5,'Geissler','Helga','1953-01-13','1978-02-14','Bochum','44809','Steinbankstr.','15','J',NULL,NULL),(6,'Westermann','Yvonne','1961-08-07','1994-10-09','Oer-Erkenschwick','45739','Ackerstr.','34','J',NULL,'M'),(7,'Karlovich','Liane','1955-05-19','1982-06-20','Hattingen','45525','Raabestr.','21','J',NULL,NULL),(8,'Meier','Norbert','1956-07-22','1984-08-23','Recklinghausen','45665','Idastr.','24','J',NULL,'M'),(9,'Ottensen','Petra','1957-09-25','1986-10-26','Herten','45699','Gablonzer Weg','27','J',NULL,NULL),(10,'Quantz','Reinhard','1958-11-28','1988-01-29','Datteln','45711','Halterner Allee','30','J',NULL,'M'),(11,'Schiller','Theresia','1959-03-31','1990-02-01','Haltern','45721','Am Freibad','32','J',NULL,NULL),(12,'Untermann','Volker','1960-04-02','1992-06-05','Waltrop','45731','Goethestr.','33','J',NULL,'M'),(13,'Westermann','Yvonne','1961-08-07','1994-10-09','Oer-Erkenschwick','45739','Ackerstr.','34','J',NULL,NULL),(14,'Xanh','Wu Dao','1962-12-11','1996-01-13','Marl','45772','Bachackerweg','35','J',NULL,'M'),(15,'Zenep','Altun','1963-02-14','1998-03-15','Gelsenkirchen','45888','Cheruskerstr.','36','J',NULL,'M'),(16,'Bronkovic','Cecilia','1964-04-16','2000-05-17','Gladbeck','45966','Dechenstr.','37','J',NULL,NULL),(17,'Deutschmann','Evelyn','1965-06-18','2002-07-19','Oberhausen','46147','Ebereschenweg','38','J',NULL,NULL),(18,'Friedrichsen','Gustav','1966-08-20','2004-09-21','Bottrop','46244','Falkenweg','39','J',NULL,'M'),(19,'Jaspers','Karol','1968-12-24','2008-01-25','Borken','46325','Heimser Weg','1','J',NULL,'M'),(20,'Liebermann','Maria','1970-02-26','1988-03-27','Velen','46342','Inselstr.','4','J',NULL,NULL),(21,'Netep','Osman','1971-05-28','1990-06-29','Raesfeld','46348','Juister Str.','7','J',NULL,'M'),(22,'Chwielorz','Kathrin','1981-08-18','2002-12-15','Köln','50173','Gartenfelder Str.','23','N',3,NULL),(23,'Schwichting','Eberhard','1985-06-27','2003-08-08','Hamburg','20444','Harvestehuder Weg','23 a','N',2,NULL);
/*!40000 ALTER TABLE `Versicherungsnehmer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Versicherungsvertrag`
--

DROP TABLE IF EXISTS `Versicherungsvertrag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Versicherungsvertrag` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Vertragsnummer` varchar(20) NOT NULL,
  `Abschlussdatum` date NOT NULL,
  `Art` char(2) NOT NULL,
  `Mitarbeiter_ID` int NOT NULL,
  `Fahrzeug_ID` int NOT NULL,
  `Versicherungsnehmer_ID` int NOT NULL,
  `Basispraemie` decimal(10,0) NOT NULL DEFAULT '500',
  `Praemiensatz` int NOT NULL DEFAULT '100',
  `Praemienaenderung` date DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Versicherungsvertrag_Nummer` (`Vertragsnummer`),
  KEY `Versicherungsvertrag_Datum` (`Abschlussdatum`),
  KEY `Versicherungsvertrag_MI` (`Mitarbeiter_ID`),
  KEY `Versicherungsvertrag_FZ` (`Fahrzeug_ID`),
  KEY `Versicherungsvertrag_VN` (`Versicherungsnehmer_ID`),
  CONSTRAINT `Versicherungsvertrag_FZ` FOREIGN KEY (`Fahrzeug_ID`) REFERENCES `Fahrzeug` (`ID`),
  CONSTRAINT `Versicherungsvertrag_MI` FOREIGN KEY (`Mitarbeiter_ID`) REFERENCES `Mitarbeiter` (`ID`),
  CONSTRAINT `Versicherungsvertrag_VN` FOREIGN KEY (`Versicherungsnehmer_ID`) REFERENCES `Versicherungsnehmer` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Versicherungsvertrag`
--

LOCK TABLES `Versicherungsvertrag` WRITE;
/*!40000 ALTER TABLE `Versicherungsvertrag` DISABLE KEYS */;
INSERT INTO `Versicherungsvertrag` VALUES (1,'DG-01','1974-05-03','TK',9,1,1,550,100,NULL),(2,'DG-02','1974-05-03','TK',9,2,1,550,100,NULL),(3,'DG-03','1974-05-03','TK',9,3,1,550,100,NULL),(4,'DH-02','1990-02-01','HP',10,12,10,500,100,NULL),(5,'DO-03','1994-10-09','HP',9,14,12,500,100,NULL),(6,'DB-04','2008-01-25','HP',9,21,19,500,100,NULL),(7,'RH-01','1976-12-11','VK',10,5,3,800,100,NULL),(8,'RD-02','1988-01-29','HP',9,11,9,500,100,NULL),(9,'RM-03','1996-01-13','HP',9,15,13,500,100,NULL),(10,'RD-04','2006-11-23','HP',9,20,18,500,100,NULL),(11,'RR-05','1990-06-29','TK',9,23,21,550,100,NULL),(12,'KB-01','1978-02-14','TK',10,6,4,550,100,NULL),(13,'KH-02','1986-10-26','HP',9,10,8,500,100,NULL),(14,'KG-03','1998-03-15','HP',9,16,14,500,100,NULL),(15,'KV-04','1988-03-27','HP',10,22,20,500,100,NULL),(16,'HE-01','1980-04-17','HP',10,7,5,500,100,NULL),(17,'HR-02','1984-08-23','HP',9,9,7,500,100,NULL),(18,'HG-03','2000-05-17','HP',9,17,15,500,100,NULL),(19,'HB-04','2004-09-21','HP',9,19,17,500,100,NULL),(20,'XC-01','1974-08-07','HP',10,4,2,500,100,NULL),(21,'XH-02','1982-06-20','VK',9,8,6,800,100,NULL),(22,'XW-03','1992-06-05','VK',10,13,11,800,100,NULL),(23,'XO-04','2002-07-19','VK',9,18,16,800,100,NULL),(24,'KNH-234','2007-03-16','TK',9,24,22,550,100,NULL),(25,'RVV-845','2003-08-08','HP',10,25,23,500,100,NULL);
/*!40000 ALTER TABLE `Versicherungsvertrag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Zuordnung_SF_FZ`
--

DROP TABLE IF EXISTS `Zuordnung_SF_FZ`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8 */;
CREATE TABLE `Zuordnung_SF_FZ` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Schadensfall_ID` int NOT NULL,
  `Fahrzeug_ID` int NOT NULL,
  `Schadenshoehe` decimal(16,2) DEFAULT NULL,
  `Schuldanteil` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Zuordnung_SF_FK` (`Schadensfall_ID`),
  KEY `Zuordnung_FZ_FK` (`Fahrzeug_ID`),
  CONSTRAINT `Zuordnung_FZ_FK` FOREIGN KEY (`Fahrzeug_ID`) REFERENCES `Fahrzeug` (`ID`),
  CONSTRAINT `Zuordnung_SF_FK` FOREIGN KEY (`Schadensfall_ID`) REFERENCES `Schadensfall` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Zuordnung_SF_FZ`
--

LOCK TABLES `Zuordnung_SF_FZ` WRITE;
/*!40000 ALTER TABLE `Zuordnung_SF_FZ` DISABLE KEYS */;
INSERT INTO `Zuordnung_SF_FZ` VALUES (1,1,2,1234.50,100),(2,2,7,852.00,0),(3,2,5,1214.00,100),(4,3,4,1438.75,20),(5,3,24,2276.85,0),(6,4,1,1234.50,0),(7,4,5,1983.00,100),(8,5,2,1251.50,80),(9,5,25,731.50,100),(10,6,3,2653.40,0),(11,6,7,1438.75,100),(12,7,6,865.00,100),(13,8,7,NULL,80);
/*!40000 ALTER TABLE `Zuordnung_SF_FZ` ENABLE KEYS */;
UNLOCK TABLES;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;