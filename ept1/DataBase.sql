-- --------------------------------------------------------
-- Host:                         localhost
-- Versión del servidor:         10.5.8-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Volcando estructura de base de datos para acortador_url
CREATE DATABASE IF NOT EXISTS `acortador_url` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `acortador_url`;

-- Volcando estructura para tabla acortador_url.shortlinks
CREATE TABLE IF NOT EXISTS `shortlinks` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `shortlink` varchar(50) NOT NULL,
  `link` varchar(255) NOT NULL,
  `user_id` int(11) unsigned zerofill DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `shortlink` (`shortlink`),
  KEY `shorlink_user_fk` (`user_id`),
  CONSTRAINT `shorlink_user_fk` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=78 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla acortador_url.shortlinks: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `shortlinks` DISABLE KEYS */;
/*!40000 ALTER TABLE `shortlinks` ENABLE KEYS */;

-- Volcando estructura para tabla acortador_url.users
CREATE TABLE IF NOT EXISTS `users` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8;

-- Volcando datos para la tabla acortador_url.users: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` (`id`, `name`, `email`, `password`) VALUES
	(1, 'user1', 'user1@gmail.com', 'Eu3jUd8EO889');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
