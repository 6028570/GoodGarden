-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Gegenereerd op: 09 apr 2024 om 21:22
-- Serverversie: 10.4.32-MariaDB
-- PHP-versie: 8.2.12

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

DROP DATABASE IF EXISTS goodgarden;
CREATE DATABASE goodgarden;

USE goodgarden;

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
-- Tabelstructuur voor tabel `care_schedules`
--

CREATE TABLE `care_schedules` (
  `plant_id` int(10) UNSIGNED NOT NULL,
  `water` int(11) DEFAULT NULL,
  `bemesting` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `care_schedules`
--

INSERT INTO `care_schedules` (`plant_id`, `water`, `bemesting`) VALUES
(1, 2, 15),
(2, 3, 10),
(3, 2, 10),
(4, 2, 15),
(5, 2, 15),
(6, 3, 15),
(7, 3, 10),
(8, 2, 15),
(9, 2, 10),
(10, 2, 10),
(11, 2, 15),
(12, 3, 15),
(13, 2, 10),
(14, 3, 15),
(15, 2, 10);

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
  `last_battery_voltage` float DEFAULT NULL,
  `device_id` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `devices`
--

INSERT INTO `devices` (`id`, `serial_number`, `name`, `label`, `last_seen`, `last_battery_voltage`, `device_id`) VALUES
(15, '0033889B1BAB1169', 'firefly2_0051', 'The Field', 1712297000, 3.92796, 256),
(16, '006FE1FC316ED7D8', 'firefly2_0111', 'The Field', 1712297257, 4.07448, 322);

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
  `id` int(11) NOT NULL,
  `plant_naam` varchar(50) DEFAULT NULL,
  `plantensoort` varchar(50) NOT NULL,
  `plant_geteelt` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `planten`
--

INSERT INTO `planten` (`id`, `plant_naam`, `plantensoort`, `plant_geteelt`) VALUES
(1, 'Tomatenplant', 'Groente', 1),

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `plants`
--

CREATE TABLE `plants` (
  `id` int(10) UNSIGNED NOT NULL,
  `name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `beschrijving` text DEFAULT NULL,
  `licht` varchar(50) DEFAULT NULL,
  `vochtigheid` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Gegevens worden geëxporteerd voor tabel `plants`
--

INSERT INTO `plants` (`id`, `name`, `type`, `beschrijving`, `licht`, `vochtigheid`) VALUES
(1, 'Tomaat', 'Groente', 'Tomaat (Solanum lycopersicum) is een veelgeteelde groenteplant in de nachtschadefamilie.', 'Volle Zon', '70'),
(2, 'Sla', 'Groente', 'Sla (Lactuca sativa) is een bladgroente die vaak wordt gebruikt in salades.', 'Gedeeltelijke Schaduw', '80'),
(3, 'Wortel', 'Groente', 'Wortel (Daucus carota) is een wortelgroente meestal oranje van kleur.', 'Volle Zon', '60'),
(4, 'Komkommer', 'Groente', 'Komkommer (Cucumis sativus) is een veel gekweekte kruipende wijnplant in de familie Cucurbitaceae.', 'Volle Zon', '65'),
(5, 'Aardappel', 'Groente', 'Aardappel (Solanum tuberosum) is een zetmeelhoudend knolgewas van de vaste plant Solanum tuberosum.', 'Gedeeltelijke Schaduw', '75'),
(6, 'Courgette', 'Groente', 'Courgette (Cucurbita pepo) is een zomerpompoen die bijna een meter lang kan worden, maar meestal onrijp wordt geoogst op 15 tot 25 cm.', 'Volle Zon', '70'),
(7, 'Spinazie', 'Groente', 'Spinazie (Spinacia oleracea) is een bladgroente afkomstig uit Centraal- en West-Azië.', 'Gedeeltelijke Schaduw', '70'),
(8, 'Paprika', 'Groente', 'Paprika (Capsicum annuum) is een fruit- en groenteplant gekweekt om zijn vruchten.', 'Volle Zon', '80'),
(9, 'Ui', 'Groente', 'Ui (Allium cepa) is een groente die de meest geteelde soort is van het geslacht Allium.', 'Volle Zon', '50'),
(10, 'Radijs', 'Groente', 'Radijs (Raphanus raphanistrum subsp. sativus) is een eetbare wortelgroente.', 'Volle Zon', '70'),
(11, 'Groene Boon', 'Groente', 'Groene bonen zijn de onrijpe, jonge vruchten en beschermende peulen van verschillende cultivars van de gewone boon.', 'Volle Zon', '75'),
(12, 'Broccoli', 'Groente', 'Broccoli (Brassica oleracea var. italica) is een koelgewas dat in het voorjaar of de herfst kan worden gekweekt.', 'Volle Zon', '75'),
(13, 'Kool', 'Groente', 'Kool (Brassica oleracea of varianten) is een bladgroente, rood of wit, een tweejarige plant die wordt geteeld als eenjarige groente.', 'Gedeeltelijke Schaduw', '80'),
(14, 'Aubergine', 'Groente', 'Aubergine (Solanum melongena) is een soort in de nachtschadefamilie die wordt gekweekt om zijn eetbare vruchten.', 'Volle Zon', '85'),
(15, 'Boerenkool', 'Groente', 'Boerenkool of bladkool (Brassica oleracea var. acephala) is een groenteplant met groene of paarse bladeren.', 'Gedeeltelijke Schaduw', '70');

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
-- Indexen voor tabel `care_schedules`
--
ALTER TABLE `care_schedules`
  ADD PRIMARY KEY (`plant_id`);

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
  ADD PRIMARY KEY (`id`);

--
-- Indexen voor tabel `plants`
--
ALTER TABLE `plants`
  ADD PRIMARY KEY (`id`);

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
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT voor een tabel `plants`
--
ALTER TABLE `plants`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

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

--
-- Beperkingen voor geëxporteerde tabellen
--

--
-- Beperkingen voor tabel `care_schedules`
--
ALTER TABLE `care_schedules`
  ADD CONSTRAINT `fk_plant_id` FOREIGN KEY (`plant_id`) REFERENCES `plants` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
