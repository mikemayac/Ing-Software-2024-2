-- Creación de la Base de Datos
CREATE DATABASE IF NOT EXISTS lab_ing_software;
USE lab_ing_software;

-- Creación del Usuario (manteniendo tu configuración original)
CREATE USER IF NOT EXISTS 'lab'@'localhost' IDENTIFIED BY 'Developer123!';
GRANT SELECT, INSERT, UPDATE, DELETE ON lab_ing_software.* TO 'lab'@'localhost';
FLUSH PRIVILEGES;

-- Tabla de Usuarios para autenticación y roles
CREATE TABLE IF NOT EXISTS `usuarios` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(255) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL, -- Se asume el almacenamiento de hashes de contraseñas
  `superUser` TINYINT(1) DEFAULT '0',
  PRIMARY KEY (`idUsuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla de Detalles de Usuario para información personal
CREATE TABLE IF NOT EXISTS `detalles_usuario` (
  `idDetalle` INT NOT NULL AUTO_INCREMENT,
  `idUsuario` INT NOT NULL,
  `nombre` VARCHAR(200) NOT NULL,
  `apPat` VARCHAR(200) NOT NULL,
  `apMat` VARCHAR(200),
  `profilePicture` VARCHAR(255), -- Almacenar la URL o referencia al archivo
  PRIMARY KEY (`idDetalle`),
  FOREIGN KEY (`idUsuario`) REFERENCES `usuarios`(`idUsuario`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla de Géneros para normalizar los géneros de películas
CREATE TABLE IF NOT EXISTS `generos` (
  `idGenero` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NOT NULL UNIQUE,
  PRIMARY KEY (`idGenero`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla de Películas normalizada con género como clave foránea
CREATE TABLE IF NOT EXISTS `peliculas` (
  `idPelicula` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(200) NOT NULL,
  `idGenero` INT,
  `duracion` INT,
  `cantidadDisponible` INT NOT NULL DEFAULT '1',
  PRIMARY KEY (`idPelicula`),
  FOREIGN KEY (`idGenero`) REFERENCES `generos`(`idGenero`) ON DELETE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla de Rentas mejorada
CREATE TABLE IF NOT EXISTS `rentar` (
  `idRentar` INT NOT NULL AUTO_INCREMENT,
  `idUsuario` INT NOT NULL,
  `idPelicula` INT NOT NULL,
  `fecha_renta` DATETIME NOT NULL,
  `dias_de_renta` INT DEFAULT '5',
  `estatus` ENUM('activo', 'finalizado', 'cancelado') DEFAULT 'activo',
  PRIMARY KEY (`idRentar`),
  FOREIGN KEY (`idUsuario`) REFERENCES `usuarios`(`idUsuario`),
  FOREIGN KEY (`idPelicula`) REFERENCES `peliculas`(`idPelicula`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
