-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema db_work
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema db_work
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `db_work` DEFAULT CHARACTER SET utf8 ;
USE `db_work` ;

-- -----------------------------------------------------
-- Table `db_work`.`tb_servico`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_work`.`tb_servico` (
  `idt_servico` INT NOT NULL AUTO_INCREMENT,
  `dsc_servico` TEXT NOT NULL,
  `vlr_servico` DECIMAL(8,2) NOT NULL,
  `tmp_servico` INT NOT NULL,
  PRIMARY KEY (`idt_servico`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_work`.`tb_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_work`.`tb_cliente` (
  `idt_cliente` INT NOT NULL AUTO_INCREMENT,
  `nme_cliente` VARCHAR(50) NOT NULL,
  `end_cliente` TEXT NOT NULL,
  `tel_cliente` VARCHAR(20) NOT NULL,
  PRIMARY KEY (`idt_cliente`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `db_work`.`ta_agendamento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `db_work`.`ta_agendamento` (
  `idt_agendamento` INT NOT NULL AUTO_INCREMENT,
  `dti_agendamento` DATETIME NOT NULL,
  `cod_servico` INT NOT NULL,
  `cod_cliente` INT NOT NULL,
  PRIMARY KEY (`idt_agendamento`),
  INDEX `fk_ta_agendamento_tb_servico_idx` (`cod_servico` ASC) VISIBLE,
  INDEX `fk_ta_agendamento_tb_cliente1_idx` (`cod_cliente` ASC) VISIBLE,
  CONSTRAINT `fk_ta_agendamento_tb_servico`
    FOREIGN KEY (`cod_servico`)
    REFERENCES `db_work`.`tb_servico` (`idt_servico`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_ta_agendamento_tb_cliente1`
    FOREIGN KEY (`cod_cliente`)
    REFERENCES `db_work`.`tb_cliente` (`idt_cliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
