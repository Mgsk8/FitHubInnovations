-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.4.28-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Volcando datos para la tabla fit_hub_innovations.administrador: ~0 rows (aproximadamente)

-- Volcando datos para la tabla fit_hub_innovations.cliente: ~3 rows (aproximadamente)
INSERT INTO `cliente` (`cedula_cliente`, `contacto_emergencia`, `limitaciones_fisicas`, `especificacion_limitacion`) VALUES
	(12548, NULL, NULL, NULL),
	(969696, 0, 'no', ''),
	(111248789, 0, 'no', '');

-- Volcando datos para la tabla fit_hub_innovations.entrenador: ~0 rows (aproximadamente)

-- Volcando datos para la tabla fit_hub_innovations.horario_dinamico: ~0 rows (aproximadamente)

-- Volcando datos para la tabla fit_hub_innovations.horario_predefinido: ~0 rows (aproximadamente)

-- Volcando datos para la tabla fit_hub_innovations.membresia_cliente: ~2 rows (aproximadamente)
INSERT INTO `membresia_cliente` (`id_membresia`, `fecha_inicio`, `fecha_fin`, `tipo_membresia`, `id_cliente`, `estado`) VALUES
	(8, '2024-11-18', '2024-12-18', 'Bronce', 12548, 'Inactivo'),
	(9, '2024-06-11', '2024-07-11', 'Plata', 969696, 'Activo');

-- Volcando datos para la tabla fit_hub_innovations.recepcionista: ~0 rows (aproximadamente)

-- Volcando datos para la tabla fit_hub_innovations.supervisor: ~0 rows (aproximadamente)

-- Volcando datos para la tabla fit_hub_innovations.usuario: ~10 rows (aproximadamente)
INSERT INTO `usuario` (`cedula_usuario`, `nombre`, `apellido`, `telefono`, `fecha_nacimiento`, `email`, `tipo_usuario`, `estado`, `password`) VALUES
	(12548, 'Deivid', 'Arcila', 56549, '2024-02-26', 'deivid123@gmail', 'Cliente', 'Inactivo', 'hola'),
	(112485, 'Miguel', 'Escobar', 68452, '2004-05-02', 'Miguelito@gmail.com', 'Recepcionista', 'Activo', 'hola'),
	(154877, 'Maria', 'Ledezma', 3158478, '2000-05-10', 'maria@hotmail.com', 'Cliente', 'Inactivo', 'hola'),
	(162323, 'Juan ', 'Bedoya', 3195482298, '2005-06-28', 'juanchobedoya4@gmail.com', 'Administrador', 'Activo', 'hola'),
	(648442, 'Estiven', 'Villada', 2360909, '2004-05-18', 'Estiven@gmail.com', 'Cliente', 'Inactivo', 'hola'),
	(969696, 'Maria', 'Ledezma', 54872148, '2011-01-05', 'maria123@gmail.com', 'Cliente', 'Inactivo', 'hola'),
	(11178964, 'Miguel Angel', 'Escobar', 32147854, '2004-11-17', 'maem1704@gmail.com', 'Administrador', 'Activo', 'hola'),
	(111248789, 'Miguelito', 'Narvaez', 315487954, '2004-01-08', 'miguel123@gmail.com', 'Cliente', 'Inactivo', 'hola'),
	(487586245, 'Mariana', 'Lopez', 3158469863, '2024-06-11', 'marianita@gmail.com', 'Supervisor', 'Activo', 'hola'),
	(1112148999, 'Korina', 'Tobar', 31548753259, '2006-06-17', 'korina@gmail.com', 'Recepcionista', 'Activo', 'hola');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
