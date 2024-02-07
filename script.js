window.addEventListener("load", function () {
    fetch("https://garden.inajar.nl/api/battery_voltage_events/?format=json", {
        headers: {
            Authorization: "Token 33bb3b42452306c58ecedc3c86cfae28ba22329c" //het token van het link zodat we authorization hebben ....
        },
        mode: "cors",
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`); 
        }
        return response.json();
    })
    .then(loadData)
    .catch(error => console.error('Error fetching data:', error)); 
});

function loadData(data) {
    apiData = data; 
    console.log("Data loaded:", apiData); 


}
