-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 20 mrt 2024 om 10:19
-- Serverversie: 10.4.32-MariaDB
-- PHP-versie: 8.2.12

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
(2185, 1710839863, '2024-03-19T09:17:43Z', 256, 4.03663),
(2186, 1710842346, '2024-03-19T09:59:06Z', 322, 4.08547);

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

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `planten`
--

CREATE TABLE `planten` (
  `id` int(20) UNSIGNED NOT NULL,
  `plant_naam` varchar(255) DEFAULT NULL,
  `plantensoort` varchar(255) DEFAULT NULL,
  `plant_geteelt` tinyint(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `planten`
--

INSERT INTO `planten` (`id`, `plant_naam`, `plantensoort`, `plant_geteelt`) VALUES
(47, 'Tomaten', 'Groente', 1),
(49, 'Komkommer', 'Groente', 1),
(50, 'Appel', 'Fruit', 1),
(51, 'Sla', 'Groente', 1),
(52, 'Wietplant', 'Onkruid', 0);

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
-- Indexen voor geëxporteerde tabellen
--

--
-- Indexen voor tabel `battery_voltage_events`
--
ALTER TABLE `battery_voltage_events`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`),
  ADD UNIQUE KEY `gateway_receive_time` (`gateway_receive_time`);

--
-- Indexen voor tabel `devices`
--
ALTER TABLE `devices`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `last_seen` (`last_seen`),
  ADD UNIQUE KEY `last_battery_voltage` (`last_battery_voltage`);

--
-- Indexen voor tabel `fetch`
--
ALTER TABLE `fetch`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`),
  ADD UNIQUE KEY `gateway_receive_time` (`gateway_receive_time`),
  ADD UNIQUE KEY `value` (`value`);

--
-- Indexen voor tabel `par_events`
--
ALTER TABLE `par_events`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`),
  ADD UNIQUE KEY `gateway_receive_time` (`gateway_receive_time`),
  ADD UNIQUE KEY `value` (`value`);

--
-- Indexen voor tabel `planten`
--
ALTER TABLE `planten`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `plant_naam` (`plant_naam`);

--
-- Indexen voor tabel `relative_humidity_events`
--
ALTER TABLE `relative_humidity_events`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`),
  ADD UNIQUE KEY `gateway_receive_time` (`gateway_receive_time`),
  ADD UNIQUE KEY `value` (`value`);

--
-- Indexen voor tabel `soil_electric_conductivity_events`
--
ALTER TABLE `soil_electric_conductivity_events`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`),
  ADD UNIQUE KEY `gateway_receive_time` (`gateway_receive_time`),
  ADD UNIQUE KEY `value` (`value`);

--
-- Indexen voor tabel `soil_relative_permittivity_events`
--
ALTER TABLE `soil_relative_permittivity_events`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`),
  ADD UNIQUE KEY `gateway_receive_time` (`gateway_receive_time`),
  ADD UNIQUE KEY `value` (`value`);

--
-- Indexen voor tabel `soil_temperature_events`
--
ALTER TABLE `soil_temperature_events`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `timestamp` (`timestamp`),
  ADD UNIQUE KEY `gateway_receive_time` (`gateway_receive_time`),
  ADD UNIQUE KEY `value` (`value`);

--
-- AUTO_INCREMENT voor geëxporteerde tabellen
--

--
-- AUTO_INCREMENT voor een tabel `battery_voltage_events`
--
ALTER TABLE `battery_voltage_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2189;

--
-- AUTO_INCREMENT voor een tabel `devices`
--
ALTER TABLE `devices`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT voor een tabel `fetch`
--
ALTER TABLE `fetch`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=100;

--
-- AUTO_INCREMENT voor een tabel `par_events`
--
ALTER TABLE `par_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT voor een tabel `planten`
--
ALTER TABLE `planten`
  MODIFY `id` int(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT voor een tabel `relative_humidity_events`
--
ALTER TABLE `relative_humidity_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT voor een tabel `soil_electric_conductivity_events`
--
ALTER TABLE `soil_electric_conductivity_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT voor een tabel `soil_relative_permittivity_events`
--
ALTER TABLE `soil_relative_permittivity_events`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT voor een tabel `soil_temperature_events`
--
ALTER TABLE `soil_temperature_events`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
