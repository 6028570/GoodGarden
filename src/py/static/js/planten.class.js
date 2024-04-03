// Definitie van de Plant klasse.
class Plant {
    // Constructor om een Plant object te initialiseren met data van een dataObject.
    constructor(dataObject) {
        // Initialiseren van de eigenschappen van de plant.
        this.id = dataObject.id;
        this.plantNaam = dataObject.plant_naam; // Naam van de plant.
        this.plantensoort = dataObject.plantensoort; // Soort van de plant.
        this.plantGeteelt = dataObject.plant_geteelt; // Geteelt status van de plant.
    }
}

class PlantGrid {
    // Constructor om een PlantGrid object te initialiseren.
    constructor() {
        this.grid = []; // De datastructuur die het raster van planten bevat.
        this.cols = 2; // Aantal kolommen in het raster.
        this.rows = 4; // Aantal rijen in het raster (inclusief de rij voor de "Toevoegen" knop).

        // Initialiseren van het raster met null waarden.
        for (let i = 0; i < this.rows; i++) {
            this.grid[i] = new Array(this.cols).fill(null);
        }

        // Laadt JSON data van de server.
        this.loadData();
    }
    
    // Methode om data te laden.
    loadData() {
        fetch('../script/plants.json') // Veronderstelt dat de JSON data is opgeslagen in 'plants.json'.
            .then(response => {
                // Controleer of de netwerkrespons ok is.
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json(); // Parse de JSON uit de respons.
            })
            .then(data => {
                // Filter de data op planten die geteeld zijn.
                const filteredData = data.filter(plantObject => plantObject.plant_geteelt === 1);

                // Vul het raster met plantobjecten.
                filteredData.slice(0, 8).forEach((plantObject, index) => {
                    const plant = new Plant(plantObject); // Maak een nieuw Plant object.
                    const col = index % this.cols; // Bereken de kolomindex.
                    const row = Math.floor(index / this.cols); // Bereken de rijindex.
                    this.grid[row][col] = plant; // Voeg de plant toe aan het raster.
                });

                // Toon het raster in de HTML tabel met id "planten".
                this.displayGrid();
            })
            .catch(error => console.error('Error loading data:', error)); // Log eventuele fouten.
    }
    

    displayGrid() {
        const plantenTable = document.getElementById("planten");

        let itemCount = 0; // Counter for the number of items in the grid

        this.grid.forEach((row, rowIndex) => {
            const tr = document.createElement("tr");

            row.forEach((plant, colIndex) => {
                const td = document.createElement("td");

                if (itemCount < 8) {
                    if (plant) {
                        // Handle regular plant items
                        const link = document.createElement("a");
                        link.href = `planteninfo.html?id=${plant.id}`; // Link naar de planteninfo pagina met plant id als query parameter

                        const article = document.createElement("article");
                        article.classList.add("plant-container");
                        link.appendChild(article); // Voeg het artikel toe aan de link

                        const img = article.appendChild(document.createElement("img"));
                        img.src = "../static/images/icon_awesome-apple-alt.png";
                        const h2 = article.appendChild(document.createElement("h2"));
                        h2.classList.add("plant-naam");
                        h2.textContent = plant.plantNaam;

                        td.appendChild(link); // Voeg de link toe aan de td
                        itemCount++;
                    } else if (rowIndex === this.rows - 1 && colIndex === this.cols - 1 && itemCount <= 7) {
                        // Handle the "Add" button
                        const article = document.createElement("article");
                        const img = article.appendChild(document.createElement("img"));
                        img.src = "../static/images/Toevoegen.png";
                        img.id = "toevoegen";
                        img.alt = "Add";
                        article.id = "modalButton";
                        article.onclick = openModal;
                
                        td.appendChild(article);
                        itemCount++;
                    }
                }

                tr.appendChild(td);
            });

            plantenTable.appendChild(tr);
        });
    
    }

    displayGrid() {
        const plantenTable = document.getElementById("planten"); // Verkrijg de tabel waarin het raster getoond moet worden.

        let itemCount = 0; // Teller voor het aantal items in het raster.

        this.grid.forEach((row, rowIndex) => {
            const tr = document.createElement("tr"); // Maak een tabelrij element.

            row.forEach((plant, colIndex) => {
                const td = document.createElement("td"); // Maak een tabeldata element.

                // Logica om plantitems of de "Toevoegen" knop te verwerken.
                if (itemCount < 8) {
                    if (plant) {
                        // Verwerk normale plantitems.
                        // Creëer een link element naar de planteninformatiepagina met plant ID als query parameter.
                        // Voeg vervolgens een artikel, afbeelding en titel toe met de plantinformatie.
                         // Handle regular plant items
                         const link = document.createElement("a");
                         link.href = `planteninfo.html?id=${plant.id}`;
 
                         const article = document.createElement("article");
                         article.classList.add("plant-container");
                         link.appendChild(article);
 
                         const img = article.appendChild(document.createElement("img"));
                         img.src = "../static/images/icon_awesome-apple-alt.png";
                         const h2 = article.appendChild(document.createElement("h2"));
                         h2.classList.add("plant-naam");
                         h2.textContent = plant.plantNaam;
 
                         td.appendChild(link);
                         itemCount++;
                        } else if (rowIndex === this.rows - 1 && colIndex === this.cols - 1 && itemCount <= 7) {
                            // Handle the "Add" button
                            const article = document.createElement("article");
                            const img = article.appendChild(document.createElement("img"));
                            img.src = "../static/images/Toevoegen.png";
                            img.id = "toevoegen";
                            img.alt = "Add";
                            article.id = "modalButton";
                            article.onclick = openModal;
                    
                            td.appendChild(article);
                            itemCount++;
                    }
                }

                tr.appendChild(td); // Voeg de td toe aan de tr.
            });

            plantenTable.appendChild(tr); // Voeg de tr toe aan de tabel.
        });
}
}

document.addEventListener("DOMContentLoaded", () => {
    const plantGrid = new PlantGrid();
});