-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 14 feb 2024 om 14:36
-- Serverversie: 10.4.28-MariaDB
-- PHP-versie: 8.2.4

DROP DATABASE IF EXISTS goodgarden;
CREATE DATABASE goodgarden;

USE goodgarden; 

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `goodgarden`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `battery_voltage_events`
--

CREATE TABLE `battery_voltage_events` (
  `id` int(10) UNSIGNED NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `gateway_receive_time` varchar(50) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `battery_voltage_events`
--

INSERT INTO `battery_voltage_events` (`id`, `timestamp`, `gateway_receive_time`, `device`, `value`) VALUES
(1, 1707825721, '2024-02-13T12:02:01Z', 256, 4.09890),
(2, 1707837460, '2024-02-13T15:17:40Z', 322, 4.10501),
(3, 1707825721, '2024-02-13T12:02:01Z', 256, 4.09890),
(4, 1707837460, '2024-02-13T15:17:40Z', 322, 4.10501),
(5, 1707825721, '2024-02-13T12:02:01Z', 256, 4.09890),
(6, 1707837460, '2024-02-13T15:17:40Z', 322, 4.10501),
(7, 1707825721, '2024-02-13T12:02:01Z', 256, 4.09890),
(8, 1707837460, '2024-02-13T15:17:40Z', 322, 4.10501),
(9, 1707825721, '2024-02-13T12:02:01Z', 256, 4.09890),
(10, 1707837460, '2024-02-13T15:17:40Z', 322, 4.10501);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `devices`
--

CREATE TABLE `devices` (
  `id` int(10) UNSIGNED NOT NULL,
  `serial_number` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `label` varchar(255) DEFAULT NULL,
  `last_seen` int(11) DEFAULT NULL,
  `last_battery_voltage` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `devices`
--

INSERT INTO `devices` (`id`, `serial_number`, `name`, `label`, `last_seen`, `last_battery_voltage`) VALUES
(1, '0033889B1BAB1169', 'firefly2_0051', 'The Field', 1707765066, 4.09768),
(2, '006FE1FC316ED7D8', 'firefly2_0111', 'The Field', 1707764966, 4.10745);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `fetch`
--

CREATE TABLE `fetch` (
  `id` int(10) UNSIGNED NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `gateway_receive_time` varchar(50) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `fetch`
--

INSERT INTO `fetch` (`id`, `timestamp`, `gateway_receive_time`, `device`, `value`) VALUES
(70, 1707851215, '2024-02-13T19:06:55Z', 322, 0.00000),
(71, 1707851215, '2024-02-13T19:06:55Z', 322, 1.52000),
(72, 1707851215, '2024-02-13T19:06:55Z', 322, 12.06000),
(73, 1707825721, '2024-02-13T12:02:01Z', 256, 4.09890),
(74, 1707837460, '2024-02-13T15:17:40Z', 322, 4.10501),
(75, 0, '', 0, 0.00000),
(76, 0, '', 0, 0.00000),
(77, 1707844638, '2024-02-13T17:17:18Z', 322, 0.00000),
(78, 1707851099, '2024-02-13T19:04:59Z', 256, 0.00000),
(79, 1707844638, '2024-02-13T17:17:18Z', 322, 71.08984),
(80, 1707851099, '2024-02-13T19:04:59Z', 256, 66.72949),
(81, 1707851215, '2024-02-13T19:06:55Z', 322, 0.00000),
(82, 1707851215, '2024-02-13T19:06:55Z', 322, 1.52000),
(83, 1707851215, '2024-02-13T19:06:55Z', 322, 12.06000),
(84, 0, '', 0, 0.00000),
(85, 0, '', 0, 0.00000),
(86, 1707844638, '2024-02-13T17:17:18Z', 322, 0.00000),
(87, 1707851099, '2024-02-13T19:04:59Z', 256, 0.00000),
(88, 1707844638, '2024-02-13T17:17:18Z', 322, 71.08984),
(89, 1707851099, '2024-02-13T19:04:59Z', 256, 66.72949),
(90, 1707825721, '2024-02-13T12:02:01Z', 256, 4.09890),
(91, 1707837460, '2024-02-13T15:17:40Z', 322, 4.10501),
(92, 0, '', 0, 0.00000),
(93, 0, '', 0, 0.00000),
(94, 1707844638, '2024-02-13T17:17:18Z', 322, 0.00000),
(95, 1707851099, '2024-02-13T19:04:59Z', 256, 0.00000),
(96, 1707844638, '2024-02-13T17:17:18Z', 322, 71.08984),
(97, 1707851099, '2024-02-13T19:04:59Z', 256, 66.72949);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `par_events`
--

CREATE TABLE `par_events` (
  `id` int(10) UNSIGNED NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `gateway_receive_time` varchar(50) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `par_events`
--

INSERT INTO `par_events` (`id`, `timestamp`, `gateway_receive_time`, `device`, `value`) VALUES
(1, 1707844638, '2024-02-13T17:17:18Z', 322, 0.00000),
(2, 1707851099, '2024-02-13T19:04:59Z', 256, 0.00000);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `relative_humidity_events`
--

CREATE TABLE `relative_humidity_events` (
  `id` int(10) UNSIGNED NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `gateway_receive_time` varchar(50) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `relative_humidity_events`
--

INSERT INTO `relative_humidity_events` (`id`, `timestamp`, `gateway_receive_time`, `device`, `value`) VALUES
(3, 1707844638, '2024-02-13T17:17:18Z', 322, 71.08984),
(4, 1707851099, '2024-02-13T19:04:59Z', 256, 66.72949),
(5, 1707844638, '2024-02-13T17:17:18Z', 322, 71.08984),
(6, 1707851099, '2024-02-13T19:04:59Z', 256, 66.72949);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `soil_electric_conductivity_events`
--

CREATE TABLE `soil_electric_conductivity_events` (
  `id` int(10) UNSIGNED NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `gateway_receive_time` varchar(50) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `soil_electric_conductivity_events`
--

INSERT INTO `soil_electric_conductivity_events` (`id`, `timestamp`, `gateway_receive_time`, `device`, `value`) VALUES
(3, 1707851215, '2024-02-13T19:06:55Z', 322, 0.00000);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `soil_relative_permittivity_events`
--

CREATE TABLE `soil_relative_permittivity_events` (
  `id` int(10) UNSIGNED NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `gateway_receive_time` varchar(50) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `soil_relative_permittivity_events`
--

INSERT INTO `soil_relative_permittivity_events` (`id`, `timestamp`, `gateway_receive_time`, `device`, `value`) VALUES
(3, 1707851215, '2024-02-13T19:06:55Z', 322, 1.52000);

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `soil_temperature_events`
--

CREATE TABLE `soil_temperature_events` (
  `id` int(10) NOT NULL,
  `timestamp` int(11) DEFAULT NULL,
  `gateway_receive_time` varchar(50) DEFAULT NULL,
  `device` int(11) DEFAULT NULL,
  `value` decimal(10,5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `soil_temperature_events`
--

INSERT INTO `soil_temperature_events` (`id`, `timestamp`, `gateway_receive_time`, `device`, `value`) VALUES
(3, 1707851215, '2024-02-13T19:06:55Z', 322, 12.06000);

--
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `battery_voltage_events`
--
ALTER TABLE `battery_voltage_events`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `devices`
--
ALTER TABLE `devices`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `fetch`
--
ALTER TABLE `fetch`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `par_events`
--
ALTER TABLE `par_events`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `relative_humidity_events`
--
ALTER TABLE `relative_humidity_events`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `soil_electric_conductivity_events`
--
ALTER TABLE `soil_electric_conductivity_events`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `soil_relative_permittivity_events`
--
ALTER TABLE `soil_relative_permittivity_events`
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `soil_temperature_events`
--
ALTER TABLE `soil_temperature_events`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `battery_voltage_events`
--
ALTER TABLE `battery_voltage_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT voor een tabel `devices`
--
ALTER TABLE `devices`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT voor een tabel `fetch`
--
ALTER TABLE `fetch`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=98;

--
-- AUTO_INCREMENT voor een tabel `par_events`
--
ALTER TABLE `par_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT voor een tabel `relative_humidity_events`
--
ALTER TABLE `relative_humidity_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT voor een tabel `soil_electric_conductivity_events`
--
ALTER TABLE `soil_electric_conductivity_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT voor een tabel `soil_relative_permittivity_events`
--
ALTER TABLE `soil_relative_permittivity_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT voor een tabel `soil_temperature_events`
--
ALTER TABLE `soil_temperature_events`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
