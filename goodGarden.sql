DROP DATABASE IF EXISTS goodgarden;
CREATE DATABASE goodgarden;

CREATE TABLE goodgarden.sensor_data (
    id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    timestamp INT,
    gateway_receive_time VARCHAR(50),
    device INT,
    value DECIMAL(10, 5),
    PRIMARY KEY (id)
);

-- Invoegen van gegevens in de 'sensor_data'-tabel
INSERT INTO goodgarden.sensor_data (timestamp, gateway_receive_time, device, value)
VALUES (1707295162, '2024-02-07T08:39:22Z', 256, 4.107448101043701),
       (1707261284, '2024-02-06T23:14:44Z', 322, 4.111111164093018);
