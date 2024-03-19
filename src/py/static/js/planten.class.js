class Plant {
    constructor(dataObject) {
        this.id = dataObject.id;
        this.plantNaam = dataObject.plantNaam;
        this.plantensoort = dataObject.plantensoort;
        this.plantGeteelt = dataObject.plantGeteelt;
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

        // Sample data
        const dataHardObject = [
            {
                "id": 1,
                "plantNaam": "Tomt",
                "plantensoort": "Groente",
                "plantGeteelt": 1
            },
            {
                "id": 2,
                "plantNaam": "Komkommer",
                "plantensoort": "Groente",
                "plantGeteelt": 1
            },
            {
                "id": 3,
                "plantNaam": "Appel",
                "plantensoort": "Groente",
                "plantGeteelt": 0
            },
            {
                "id": 4,
                "plantNaam": "KwamKwammer",
                "plantensoort": "Groente",
                "plantGeteelt": 1
            },
            {
                "id": 5,
                "plantNaam": ":p",
                "plantensoort": "Groente",
                "plantGeteelt": 1
            },
            {
                "id": 6,
                "plantNaam": ":3",
                "plantensoort": "Groente",
                "plantGeteelt": 1
            },
            {
                "id": 7,
                "plantNaam": "Groene",
                "plantensoort": "Groente",
                "plantGeteelt": 0
            },
            {
                "id": 8,
                "plantNaam": "test",
                "plantensoort": "Groente",
                "plantGeteelt": 0
            },
            {
                "id": 9,
                "plantNaam": "yippie",
                "plantensoort": "Groente",
                "plantGeteelt": 0
            }
        ];

        // Only save objects that have plantGeteelt as 1
        const filteredData = dataHardObject.filter(plantObject => plantObject.plantGeteelt === 1);

        // Populate the grid with plant objects
        filteredData.slice(0, 8).forEach((plantObject, index) => {
            const plant = new Plant(plantObject);
            const col = index % this.cols;
            const row = Math.floor(index / this.cols);
            this.grid[row][col] = plant;
        });
        

        // Display the grid in the HTML table with id "planten"
        this.displayGrid();
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
                        const article = document.createElement("article");
                        const img = article.appendChild(document.createElement("img"));
                        img.src = "../static/images/icon_awesome-apple-alt.png";
                        const h2 = article.appendChild(document.createElement("h2"));
                        h2.classList.add("plant-naam");
                        h2.textContent = plant.plantNaam;

                        td.appendChild(article);
                        itemCount++;
                    } else if (rowIndex === this.rows -1 && colIndex === this.cols -1 && itemCount <= 7) {
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
