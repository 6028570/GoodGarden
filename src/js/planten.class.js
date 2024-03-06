dataHardObject = [
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
    }
]

class Plant {
    constructor(dataObject) {
      this.id = dataObject.id;
      this.plantNaam = dataObject.plantNaam;
      this.plantensoort = dataObject.plantensoort;
      this.plantGeteelt = dataObject.plantGeteelt;
    }

    htmlData() {
        if (this.plantGeteelt) 
        {
            const titel = document.querySelectorAll(".plant-naam");
                // titel.forEach(element => {
                // element.textContent = this.plantNaam;
                for (let i = 0; i < titel.length; i++) {
                    const element = titel[i];
                    element.textContent = this.plantNaam;
                }
            // });
        }
    }
}

// document.addEventListener('DOMContentLoaded', (event) => {
//     const tomaatPlant = new Plant(dataHardObject[0]);
//     tomaatPlant.htmlData();
// });

document.addEventListener("DOMContentLoaded", (event) => {
    dataHardObject.forEach(plantObject => {
        const plant = new Plant(plantObject);
        plant.htmlData();
    });
})