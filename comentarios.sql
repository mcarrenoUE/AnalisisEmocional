-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-03-2025 a las 04:55:23
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `sentimentdb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `comentarios`
--

CREATE TABLE `comentarios` (
  `id` int(11) NOT NULL,
  `texto` text NOT NULL,
  `sentimiento` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `comentarios`
--

INSERT INTO `comentarios` (`id`, `texto`, `sentimiento`) VALUES
(1, 'Me encanta este producto, es increíble.', 'neutral'),
(2, 'Este producto es una porquería, no lo recomiendo.', 'negativo'),
(3, 'No me gusta esto', 'negativo'),
(4, 'si me gusta mucho', 'neutral'),
(5, 'me encanta muchisimo esto', 'neutral'),
(6, 'me encanta muchisimo esto', 'neutral'),
(7, 'Odio esto', 'neutral'),
(8, 'No me gusta\n', 'negativo'),
(9, 'No me gusta', 'negativo'),
(10, 'Me encantaa', 'neutral'),
(11, 'Me encantaa', 'neutral'),
(12, 'Me gusta', 'neutral'),
(13, 'Me gusta', 'neutral'),
(14, 'LO AMOO', 'neutral'),
(15, 'LO AMOO', 'neutral'),
(16, 'Ay no se', 'negativo'),
(17, 'Soy feliz', 'neutral'),
(18, 'Soy feliz', 'neutral'),
(19, 'NO', 'negativo'),
(20, 'SI', 'neutral'),
(21, 'NO', 'negativo'),
(22, 'SI', 'neutral'),
(23, 'SI', 'neutral'),
(24, 'ENCANTADA', 'neutral'),
(25, 'ENCANTADA', 'neutral'),
(26, 'ENCANTADA', 'neutral'),
(27, 'FEO', 'neutral'),
(28, 'FEO', 'neutral'),
(29, 'FEO', 'neutral'),
(30, 'Me encanta este producto', 'neutral'),
(31, 'Me encanta este producto', 'neutral'),
(32, 'ODIO', 'neutral'),
(33, 'ODIO', 'neutral'),
(34, 'ODIO', 'neutral'),
(35, 'ODIO', 'neutral'),
(36, 'Odio', 'neutral'),
(37, 'No me gusta', 'negativo'),
(38, 'Me encanta este producto', 'neutral'),
(39, 'Me encanta este producto, es increible', 'neutral'),
(40, 'Me encanta este producto, es increible', 'neutral'),
(41, 'Increible', 'neutral'),
(42, 'Increible', 'neutral'),
(43, 'Feo', 'neutral'),
(44, 'No me gusta este producto', 'negativo'),
(45, 'Si, me gusta mucho este producto', 'neutral'),
(47, 'Hola, no me gusta', 'negativo'),
(48, 'Hola, si me gusta mucho', 'neutral'),
(49, 'Me encanta', 'neutral'),
(50, 'Es fascinante', 'positivo'),
(51, 'Fascinante', 'positivo'),
(52, 'feo', 'neutral'),
(53, 'feo', 'neutral'),
(54, 'Odio', 'neutral'),
(55, 'Odio', 'neutral'),
(56, 'No me gusta', 'negativo'),
(57, 'Me encanta este producto, es increible', 'neutral'),
(58, 'Esta muy feo, no me gusta', 'negativo'),
(59, 'Me encanta es fascinante', 'positivo'),
(60, 'Me siento triste', 'negativo'),
(61, 'me siento bien', 'neutral'),
(62, 'me siento super feliz', 'positivo'),
(63, 'me quiero morir', 'neutral'),
(64, 'Horrible', 'negativo'),
(65, 'Bien', 'neutral'),
(66, 'Buenisimo', 'neutral'),
(67, 'Super bueno', 'positivo'),
(68, 'Me siento muy mal', 'neutral'),
(69, 'Me siento mal', 'neutral'),
(70, 'Me siento mal', 'neutral'),
(71, 'Me siento peor', 'negativo'),
(72, 'Me siento bien', 'neutral'),
(73, 'soy feliz', 'neutral'),
(74, 'Me encanta esto, de verdad es fascinante', 'positivo'),
(75, 'Me siento mal, la vida no vale la pena', 'negativo'),
(76, 'Me siento mal, la vida no vale la pena', 'negativo'),
(77, 'Estoy muy triste', 'negativo'),
(78, 'estoy muy triste', 'negativo'),
(79, 'estoy muy feliz', 'neutral'),
(80, 'Estoy muy triste', 'negativo'),
(81, 'Estoy FELIZ', 'neutral'),
(82, 'Hoy es un gran día', 'neutral'),
(83, 'No sé qué pensar', 'negativo'),
(84, 'ES FASCINANTE', 'positivo'),
(85, 'MAL', 'neutral'),
(86, 'TRISTE', 'negativo'),
(88, 'ha sido un dia largo, muy triste y ha sido dificil de seguir, me siento triste', 'negativo'),
(89, 'ha sido un dia largo, me siento un poco cansado y triste', 'positivo'),
(90, ' poco cansado y triste', 'negativo'),
(91, 'Triste', 'negativo'),
(92, 'Estoy triste', 'negativo'),
(93, 'estoy triste', 'negativo'),
(94, 'Me siento triste', 'negativo'),
(95, 'Me siento mal', 'neutral'),
(96, 'me siento muy triste', 'negativo'),
(97, 'triste', 'negativo'),
(98, 'triste', 'negativo'),
(99, 'triste', 'negativo'),
(100, 'He estado triste y me ha ido mal con diferentes cosas', 'positivo'),
(101, 'triste', 'negativo'),
(102, 'he estado un poco triste', 'negativo'),
(103, 'me siento bien', 'neutral'),
(104, 'me siento muy feliz', 'neutral'),
(105, 'Me siento feliz', 'neutral'),
(106, 'Me siento feliz, ha sido un dia fascinante', 'positivo'),
(107, 'Bien', 'neutral'),
(108, 'normal', 'neutral'),
(109, 'jaja', 'neutral'),
(110, 'esta bien', 'neutral'),
(111, 'ok', 'positivo'),
(112, 'triste', 'negativo'),
(113, 'Me siento bien', 'neutral'),
(114, 'me siento bien, relajada', 'neutral'),
(115, 'me siento normal', 'neutral'),
(116, 'me siento bien', 'neutral'),
(117, 'Me siento triste', 'negativo'),
(118, 'Me siento bien', 'neutral'),
(119, 'Me siento super feliz', 'positivo'),
(120, 'Me siento triste, todo sale mal', 'negativo');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `comentarios`
--
ALTER TABLE `comentarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
