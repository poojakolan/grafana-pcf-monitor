-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema grafana
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema grafana
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `grafana` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema grafana
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema grafana
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `grafana` DEFAULT CHARACTER SET latin1 ;
USE `grafana` ;

-- -----------------------------------------------------
-- Table `grafana`.`tbl_object`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`tbl_object` (
  `id` INT(11) NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `description` VARCHAR(45) NULL DEFAULT NULL,
  `type` VARCHAR(45) NULL DEFAULT NULL,
  `image` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `grafana`.`tbl_properties`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`tbl_properties` (
  `id` INT(11) NOT NULL,
  `key` VARCHAR(45) NULL DEFAULT NULL,
  `display_name` VARCHAR(45) NULL DEFAULT NULL,
  `type` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `grafana`.`tbl_property_list`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`tbl_property_list` (
  `id` INT(11) NOT NULL,
  `object_id` INT(11) NULL DEFAULT NULL,
  `property` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tbl_property_list_tbl_object_idx` (`object_id` ASC) ,
  INDEX `fk_tbl_property_list_tbl_properties1_idx` (`property` ASC) ,
  CONSTRAINT `fk_tbl_property_list_tbl_object`
    FOREIGN KEY (`object_id`)
    REFERENCES `grafana`.`tbl_object` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_tbl_property_list_tbl_properties1`
    FOREIGN KEY (`property`)
    REFERENCES `grafana`.`tbl_properties` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `grafana`.`tbl_property_values`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`tbl_property_values` (
  `id` INT(11) NOT NULL,
  `param_value` VARCHAR(45) NULL DEFAULT NULL,
  `property_id` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tbl_property_values_tbl_properties1_idx` (`property_id` ASC) ,
  CONSTRAINT `fk_tbl_property_values_tbl_properties1`
    FOREIGN KEY (`property_id`)
    REFERENCES `grafana`.`tbl_properties` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;

USE `grafana` ;

-- -----------------------------------------------------
-- Table `grafana`.`diego_cell_health`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`diego_cell_health` (
  `id` INT(11) NOT NULL,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `ip` VARCHAR(45) NULL DEFAULT NULL,
  `job` VARCHAR(45) NULL DEFAULT NULL,
  `deployment` VARCHAR(45) NULL DEFAULT NULL,
  `mem_chunks_no` INT(11) NULL DEFAULT NULL,
  `chunk_size` INT(11) NULL DEFAULT NULL,
  `total_disk` VARCHAR(45) NULL DEFAULT NULL,
  `total_memory` INT(11) NULL DEFAULT NULL,
  `avail_disk_per` DECIMAL(10,0) NULL DEFAULT NULL,
  `avail_mem_per` DECIMAL(10,0) NULL DEFAULT NULL,
  `is_historic` VARCHAR(1) NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `grafana`.`foundries`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`foundries` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `foundry_name` VARCHAR(45) NULL DEFAULT NULL,
  `memory_consumption_percent` INT(11) NOT NULL,
  `foundry_memory` DOUBLE NULL DEFAULT NULL,
  `is_historic` VARCHAR(1) NULL DEFAULT NULL,
  `last_updated` DATETIME NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) )
ENGINE = InnoDB
AUTO_INCREMENT = 11
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `grafana`.`mysql_health`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`mysql_health` (
  `id` INT(11) NOT NULL,
  `total_node_no` INT(11) NULL DEFAULT NULL,
  `healthy_node_no` INT(11) NULL DEFAULT NULL,
  `is_historic` VARCHAR(1) NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
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
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
  INDEX `foundry_id_idx` (`foundry_id` ASC) ,
  CONSTRAINT `foundry_id`
    FOREIGN KEY (`foundry_id`)
    REFERENCES `grafana`.`foundries` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 33
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
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
  INDEX `org_fkey_idx` (`org_id` ASC) ,
  CONSTRAINT `org_fkey`
    FOREIGN KEY (`org_id`)
    REFERENCES `grafana`.`pcf_org` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 44
DEFAULT CHARACTER SET = latin1;


-- -----------------------------------------------------
-- Table `grafana`.`pcf_apps`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grafana`.`pcf_apps` (
  `id` BIGINT(225) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NULL DEFAULT NULL,
  `memory` DECIMAL(20,0) NULL DEFAULT NULL,
  `instances` TINYINT(10) NULL DEFAULT NULL,
  `disk_space` INT(11) NULL DEFAULT NULL,
  `state` VARCHAR(20) NULL DEFAULT NULL,
  `cpu_used` DECIMAL(20,15) NULL DEFAULT NULL,
  `memory_used` DECIMAL(20,2) NULL DEFAULT NULL,
  `disk_used` DECIMAL(20,0) NULL DEFAULT NULL,
  `space_id` INT(11) NULL DEFAULT NULL,
  `memory_consumption_percent` INT(11) NOT NULL,
  `last_updated` DATETIME NOT NULL,
  `is_historic` VARCHAR(1) NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) ,
  INDEX `space_fkey_idx` (`space_id` ASC) ,
  CONSTRAINT `space_fkey`
    FOREIGN KEY (`space_id`)
    REFERENCES `grafana`.`pcf_space` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 41
DEFAULT CHARACTER SET = latin1;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
