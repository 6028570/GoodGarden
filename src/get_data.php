<?php
// Database-verbinding instellen (vervang deze gegevens door je eigen databasegegevens)
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "goodgarden";

// Verbinding maken met de database
$conn = new mysqli($servername, $username, $password, $dbname);

// Controleren op een geslaagde verbinding
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Query om gegevens op te halen uit de tabel devices
$query_devices = "SELECT * FROM devices";
$result_devices = $conn->query($query_devices);

// Query om gegevens op te halen uit de tabel battery_voltage_events
$query_battery_voltage = "SELECT * FROM battery_voltage_events";
$result_battery_voltage = $conn->query($query_battery_voltage);

// Query om gegevens op te halen uit de tabel fetch
$query_fetch = "SELECT * FROM fetch";
$result_fetch = $conn->query($query_fetch);

// Array om resultaten op te slaan
$data = array();

// Controleren of er resultaten zijn van de tabel devices
if ($result_devices->num_rows > 0) {
    $data['devices'] = $result_devices->fetch_all(MYSQLI_ASSOC);
}

// Controleren of er resultaten zijn van de tabel battery_voltage_events
if ($result_battery_voltage->num_rows > 0) {
    $data['battery_voltage_events'] = $result_battery_voltage->fetch_all(MYSQLI_ASSOC);
}

// Controleren of er resultaten zijn van de tabel fetch
if ($result_fetch->num_rows > 0) {
    $data['fetch'] = $result_fetch->fetch_all(MYSQLI_ASSOC);
}

// Gegevens als JSON-uitvoer
echo json_encode($data);

// Verbinding sluiten
$conn->close();
