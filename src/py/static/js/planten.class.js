class Plant {
    constructor(dataObject) {
        this.id = dataObject.id;
        this.plantNaam = dataObject.plant_naam; // Note the property name change
        this.plantensoort = dataObject.plantensoort;
        this.plantGeteelt = dataObject.plant_geteelt;
    }
}

class PlantGrid {
    constructor() {
        this.grid = [];
        this.cols = 2; // Number of columns
        this.rows = 4; // Number of rows (including the row for the "Add" button)

        // Initialize the grid with null values
        for (let i = 0; i < this.rows; i++) {
            this.grid[i] = new Array(this.cols).fill(null);
        }

        // Load JSON data from the server
        this.loadData();
    }

    loadData() {
        fetch('../script/plants.json') // Assuming your JSON data is stored in 'plants.json'
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                const filteredData = data.filter(plantObject => plantObject.plant_geteelt === 1);

                // Populate the grid with plant objects
                filteredData.slice(0, 8).forEach((plantObject, index) => {
                    const plant = new Plant(plantObject);
                    const col = index % this.cols;
                    const row = Math.floor(index / this.cols);
                    this.grid[row][col] = plant;
                });

                // Display the grid in the HTML table with id "planten"
                this.displayGrid();
            })
            .catch(error => console.error('Error loading data:', error));
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
}

document.addEventListener("DOMContentLoaded", () => {
    const plantGrid = new PlantGrid();
});
