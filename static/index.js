function executeOperation(operationChoice) {
    fetch(`/battery_voltage_events?operation=${operationChoice}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();  // Gebruik response.json() om JSON-gegevens te parsen
        })
        .then(data => {
            // Verwerk de gegevens zoals nodig
            console.log(data);  // Bekijk de gegevens in de console
        })
        .catch(error => {
            console.error('Error:', error);
            alert(`An error occurred: ${error.message}`);
        });
}
