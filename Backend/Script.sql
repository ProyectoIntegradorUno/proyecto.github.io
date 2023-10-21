-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Empresa
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Empresa
-- -----------------------------------------------------
CREATE SCHEMA  `Empresa` DEFAULT CHARACTER SET utf8 ;
USE `Empresa` ;

-- -----------------------------------------------------
-- Table `Empresa`.`tipoProductos`
-- -----------------------------------------------------
CREATE TABLE `Empresa`.`tipoProductos` (
  `idtipoProductos` INT NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`idtipoProductos`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Empresa`.`Productos`
-- -----------------------------------------------------
CREATE TABLE `Empresa`.`Productos` (
  `idProductos` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(200) NOT NULL,
  `unidad` VARCHAR(45) NOT NULL,
  `imagen` LONGBLOB NOT NULL,
  `precio` FLOAT NOT NULL,
  `tipo` INT NOT NULL,
  PRIMARY KEY (`idProductos`),
  INDEX `tipoproductos_idx` (`tipo` ASC) VISIBLE,
  CONSTRAINT `tipoproductos`
    FOREIGN KEY (`tipo`)
    REFERENCES `Empresa`.`tipoProductos` (`idtipoProductos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Empresa`.`Clientes`
-- -----------------------------------------------------
CREATE TABLE  `Empresa`.`Clientes` (
  `cuit` VARCHAR(11) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `mail` VARCHAR(45) NOT NULL,
  `domicilio_fiscal` VARCHAR(45) NOT NULL,
  `domicilio_de_entrega` VARCHAR(45) NOT NULL,
  `telefono` VARCHAR(45) NOT NULL,
  `password` VARCHAR(30) NOT NULL,
  `codigo_de_vereficacion` INT NOT NULL,
  `vereficado` TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY (`cuit`),
  UNIQUE INDEX `mail_UNIQUE` (`mail` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Empresa`.`Facturas`
-- -----------------------------------------------------
CREATE TABLE  `Empresa`.`Facturas` (
  `idFactura` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NOT NULL,
  `modo_de_pago` VARCHAR(45) NOT NULL,
  `cuit` VARCHAR(11) NOT NULL,
  PRIMARY KEY (`idFactura`),
  INDEX `cuit_idx` (`cuit` ASC) VISIBLE,
  CONSTRAINT `cuit`
    FOREIGN KEY (`cuit`)
    REFERENCES `Empresa`.`Clientes` (`cuit`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Empresa`.`itemsFactura`
-- -----------------------------------------------------
CREATE TABLE  `Empresa`.`itemsFactura` (
  `iditems` INT NOT NULL AUTO_INCREMENT,
  `cantidad` INT NOT NULL,
  `precio` FLOAT NOT NULL,
  `idproducto` INT NOT NULL,
  `idfactura` INT NOT NULL,
  PRIMARY KEY (`iditems`),
  INDEX `idProductos_idx` (`idproducto` ASC) VISIBLE,
  INDEX `idFactura_idx` (`idfactura` ASC) VISIBLE,
  CONSTRAINT `idProductos`
    FOREIGN KEY (`idproducto`)
    REFERENCES `Empresa`.`Productos` (`idProductos`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `idFactura`
    FOREIGN KEY (`idfactura`)
    REFERENCES `Empresa`.`Facturas` (`idFactura`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Empresa`.`roles`
-- -----------------------------------------------------
CREATE TABLE  `Empresa`.`roles` (
  `idrol` INT NOT NULL,
  `descripcion` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`idrol`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Empresa`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE  `Empresa`.`Usuarios` (
  `cuitUsuario` INT UNSIGNED NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  `rol` INT NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`cuitUsuario`),
  INDEX `rol_idx` (`rol` ASC) VISIBLE,
  CONSTRAINT `rol`
    FOREIGN KEY (`rol`)
    REFERENCES `Empresa`.`roles` (`idrol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;



