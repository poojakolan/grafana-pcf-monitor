-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema grafana
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema grafana
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `grafana` DEFAULT CHARACTER SET latin1 ;
USE `grafana` ;

-- -----------------------------------------------------
-- Table `grafana`.`foundries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`foundries` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `foundry_name` VARCHAR(45) NULL DEFAULT NULL,
  `memory_consumption_percent` INT(11) NOT NULL,
  `last_updated` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE)
ENGINE = InnoDB
AUTO_INCREMENT = 5
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `grafana`.`pcf_org`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`pcf_org` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `org_name` VARCHAR(100) NOT NULL,
  `foundry_id` INT(11) NULL DEFAULT NULL,
  `memory_consumption_percent` INT(11) NOT NULL,
  `last_updated` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`, `org_name`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `foundry_id_idx` (`foundry_id` ASC) VISIBLE,
  CONSTRAINT `foundry_id`
    FOREIGN KEY (`foundry_id`)
    REFERENCES `grafana`.`foundries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 21
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `grafana`.`pcf_space`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`pcf_space` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `space_name` VARCHAR(100) NULL DEFAULT NULL,
  `org_id` INT(11) NULL DEFAULT NULL,
  `memory_consumption_percent` INT(11) NOT NULL,
  `last_updated` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `org_fkey_idx` (`org_id` ASC) VISIBLE,
  CONSTRAINT `org_fkey`
    FOREIGN KEY (`org_id`)
    REFERENCES `grafana`.`pcf_org` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 20
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `grafana`.`pcf_apps`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`pcf_apps` (
  `id` BIGINT(225) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `memory` DECIMAL(10,0) NULL DEFAULT NULL,
  `instances` TINYINT(10) NULL DEFAULT NULL,
  `disk_space` INT(11) NULL DEFAULT NULL,
  `state` VARCHAR(20) NULL DEFAULT NULL,
  `cpu_used` DECIMAL(20,15) NULL DEFAULT NULL,
  `memory_used` DECIMAL(10,0) NULL DEFAULT NULL,
  `disk_used` DECIMAL(10,0) NULL DEFAULT NULL,
  `space_id` INT(11) NULL DEFAULT NULL,
  `memory_consumption_percent` INT(11) NOT NULL,
  `last_updated` DATETIME NOT NULL,
  `is_historic` VARCHAR(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  INDEX `space_fkey_idx` (`space_id` ASC) VISIBLE,
  CONSTRAINT `space_fkey`
    FOREIGN KEY (`space_id`)
    REFERENCES `grafana`.`pcf_space` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
