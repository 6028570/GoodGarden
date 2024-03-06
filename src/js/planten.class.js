dataHardObject = {
    "id": 1,
    "plantnaam": "Tomaat",
    "plantensoort": "Groente",
    "plantGeteelt": 1
}

// Nieuwe planten aanmaken in de table
// function hardcodeData(dataHardObject) 
// {
//     dataHardObject => "id"    
// }

class Plant {
    constructor(dataHardObject) {
      this.id = dataHardObject.id;
      this.plantNaam = dataHardObject.plantNaam;
      this.plantensoort = dataHardObject.plantensoort;
      this.plantGeteelt = dataHardObject.plantGeteelt;
    }

    htmlData(plantNaam) {
        if (this.plantGeteelt) 
        {
            const titel = document.querySelector(".plant-naam");
            titel.textContent = this.plantNaam;
        }
    }
}

const tomaatPlant = new Plant(dataHardObject);
tomaatPlant.htmlData();