# Importeer de json en mysql.connector modules voor het werken met JSON data en MySQL databases.
# Importeer ook os voor bestandssysteem operaties.
import json
import mysql.connector
import os

# Functie om een verbinding met de database te maken.
def database_connect():
    return mysql.connector.connect(
        host="localhost",  # De server waar de database draait.
        user="root",       # De gebruikersnaam om in te loggen op de database.
        password="",       # Het wachtwoord voor de gebruiker.
        database="goodgarden"  # De naam van de database waarmee verbinding moet worden gemaakt.
    )

# Functie om het absolute pad van de huidige directory te krijgen.
def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

# Functie om plantgegevens uit de database te halen en naar een JSON-bestand te schrijven.
def fetch_plant_and_write_to_json():
    # Maak verbinding met de database.
    connection = database_connect()
    
    try:
        # Maak een cursorobject aan met dictionary=True om rijen als woordenboeken op te halen.
        cursor = connection.cursor(dictionary=True)
        # Voer de SQL-query uit om gegevens op te halen.
        cursor.execute("SELECT id, plant_naam, plantensoort, plant_geteelt FROM planten")
        # Haal alle rijen op.
        plants = cursor.fetchall()
        
        # Verkrijg het absolute pad van de huidige directory.
        current_directory = get_current_directory()
        # Construeer het absolute pad voor het JSON-bestand.
        json_file_path = os.path.join(current_directory, 'plants.json')
        
        # Schrijf de opgehaalde gegevens naar een JSON-bestand.
        with open(json_file_path, 'w') as json_file:
            json.dump(plants, json_file, indent=4)
            
    except mysql.connector.Error as error:
        # Print de fout als er iets misgaat bij het ophalen van de gegevens.
        print("Error fetching data from MySQL table:", error)
        
    finally:
        # Sluit de cursor en de verbinding, indien ze bestaan.
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()

# Roept de functie aan om gegevens op te halen en naar JSON te schrijven.
fetch_plant_and_write_to_json()