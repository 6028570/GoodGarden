import sys
import json

from db_connect import database_connect
from mysql.connector import Error

# Voeg de data uit het formulier toe aan de database
def insert_plant_name(plant_naam, plantensoort, plant_geteelt):

    # Als er "true" is meegegeven als waarde dan komt in de database 1 anders 0 (false)
    plant_geteelt_value = 1 if plant_geteelt.lower() == "true" else 0

    try:
        # Gebruik de verbinding die teruggegeven wordt door de database_connect functie uit de db_connect module
        connection = database_connect()

        # Je kunt de controle of de verbinding succesvol is rechtstreeks in de database_connect functie uitvoeren
        # De cursor() zorgt ervoor dat er een verbinding met de database gelegd kan worden en de data gemanipuleerd
        cursor = connection.cursor()
        query = "INSERT INTO goodgarden.planten (plant_naam, plantensoort, plant_geteelt) VALUES (%s, %s, %s)"
        cursor.execute(query, (plant_naam, plantensoort, plant_geteelt_value))  # "%s" wordt hier ingevuld doormiddel van de variable (parameter)
        connection.commit()
        print(json.dumps({"success": True}))
    
    except Error as e:
        print(json.dumps({"success": False, "error": str(e)}))
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
        
# Wordt alleen uitgevoerd als het een standalone script is (geen import!!!) 
if __name__ == "__main__":
    # Dit zijn de variables die door het JavaScript bestand (app.js) worden meegegeven --- NOTE: sys.argv[0] is altijd de naam van het script!
    plant_naam = sys.argv[1]
    plantensoort = sys.argv[2]
    plant_geteelt = sys.argv[3]

    # Call de function met de variables
    insert_plant_name(plant_naam, plantensoort, plant_geteelt)