-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: restaurante_bd
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `mesa`
--

DROP TABLE IF EXISTS `mesa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesa` (
  `cod` int(11) NOT NULL AUTO_INCREMENT,
  `valor` double DEFAULT NULL,
  `pedidos` text,
  `valores` text,
  PRIMARY KEY (`cod`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesa`
--

LOCK TABLES `mesa` WRITE;
/*!40000 ALTER TABLE `mesa` DISABLE KEYS */;
INSERT INTO `mesa` VALUES (1,90,'*Pizza portuguesa\n*Pizza de calabresa\n',' x 3 - 45.0\n x 3 - 45.0\n'),(2,0,NULL,NULL),(3,0,NULL,NULL),(4,0,NULL,NULL),(5,0,NULL,NULL),(6,0,NULL,NULL),(7,0,NULL,NULL),(8,0,NULL,NULL),(9,0,NULL,NULL),(10,0,NULL,NULL);
/*!40000 ALTER TABLE `mesa` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `atualiza_valor` BEFORE UPDATE ON `mesa` FOR EACH ROW begin 
	if new.valor!=old.valor and new.valor>0 then
		set new.valor=old.valor+new.valor;
        if old.pedidos is null then
			set new.pedidos=concat('',new.pedidos);
            set new.valores=concat('',new.valores);
		else
			set new.pedidos=concat(old.pedidos,new.pedidos);
            set new.valores=concat(old.valores,new.valores);
		end if;
	end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `prato`
--

DROP TABLE IF EXISTS `prato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prato` (
  `cod` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `preco` double DEFAULT NULL,
  `tipo` int(11) DEFAULT NULL,
  `imagem` text,
  PRIMARY KEY (`cod`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prato`
--

LOCK TABLES `prato` WRITE;
/*!40000 ALTER TABLE `prato` DISABLE KEYS */;
INSERT INTO `prato` VALUES (1,'Pizza portuguesa',15,1,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\pizzaPT.jpg'),(2,'Pizza de calabresa',15,1,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\pizzacb.jpg'),(3,'Pizza de frango',15,1,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\pizza-de-frango-com-catupiry-18845.jpg'),(4,'Pizza mista',15,1,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\mista.jpg'),(5,'Lasanha',20,1,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\lasanha.jpg'),(6,'Spaghetti',17,1,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\spaghetti.jpg'),(7,'Suco de laranja',5,3,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\sucolaranja.jpg'),(8,'Suco de limão',5,3,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\limao.jpg'),(9,'Água indaia 500ml',1,3,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\indaia.jpg'),(10,'Coca cola 1L',5,3,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\coca.jpg'),(11,'Cerveja Skol 900ml',5,3,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\skol.jpg'),(12,'Cerveja Itaipava 900ml',5,3,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\itaipava.jpg'),(13,'Maminha 1Kg',10,4,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\maminha.jpg'),(14,'Alcatra 1Kg',10,4,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\alcatra.jpg'),(15,'Costela 1Kg',10,4,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\costela.jpg'),(16,'Contra filé 1Kg',10,4,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\contrafile.jpg'),(17,'Picanha 1Kg',10,4,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\picanha.jpg'),(18,'Yakisoba',12,2,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\yakisoba.jpg'),(19,'Baião de dois',12,5,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\baiao.jpg'),(20,'Cuscuz',11,5,'\\Users\\RENÊ MICHEL\\Pictures\\BD\\cuscuz.jpg');
/*!40000 ALTER TABLE `prato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipo`
--

DROP TABLE IF EXISTS `tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipo` (
  `cod` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`cod`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipo`
--

LOCK TABLES `tipo` WRITE;
/*!40000 ALTER TABLE `tipo` DISABLE KEYS */;
INSERT INTO `tipo` VALUES (1,'Italiana'),(2,'Japonesa'),(3,'Bebidas'),(4,'Carnes'),(5,'Nordestina');
/*!40000 ALTER TABLE `tipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'restaurante_bd'
--

--
-- Dumping routines for database 'restaurante_bd'
--
/*!50003 DROP PROCEDURE IF EXISTS `cadastrar_prato` */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
CREATE DEFINER=`root`@`localhost` PROCEDURE `cadastrar_prato`(nome_ varchar(255),tipo_ varchar(255),valor double,img text)
begin
	declare codigo int;
    select cod into codigo from tipo where nome=tipo_;
    if codigo is not null then
		insert into prato(nome,preco,tipo,imagem)values(nome_,valor,codigo,img);
	else
		insert into tipo(nome)values(tipo_);
        select cod into codigo from tipo where nome=tipo_;
		insert into prato(nome,preco,tipo,imagem)values(nome_,valor,codigo,img);
	end if;
end ;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-12-05 23:37:08
