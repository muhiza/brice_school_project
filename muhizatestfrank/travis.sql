# Create Testuser
CREATE USER 'dev'@'localhost' IDENTIFIED BY 'dev';
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON *.* TO 'dev'@'localhost';
# Create DB
CREATE DATABASE IF NOT EXISTS `demo` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `demo`;
# Create Table


CREATE TABLE IF NOT EXISTS `employees` (
  `id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
# Add Data



CREATE TABLE IF NOT EXISTS `departments` (
  `id` int(11) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `departments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
# Add Data



CREATE TABLE IF NOT EXISTS `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL

) ENGINE=InnoDB DEFAULT CHARSET=utf8;
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
# Add Data
