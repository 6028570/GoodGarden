# Importeer de benodigde modules voor MySQL connectiviteit.
import mysql.connector
from mysql.connector import Error

def database_connect():
    """
    Maakt verbinding met de MySQL database.

    Probeert een verbinding met de MySQL-database op te zetten met behulp van
    de mysql.connector.connect methode, gebruikmakend van de database
    credentials. Bij succes retourneert het de verbinding; bij een mislukking
    vangt het de fout op en print een bericht.

    Returns:
        connection (mysql.connector.connect object): Een connectie object als
        de verbinding succesvol is. Anders None.
    """
    try:
        # Probeert een verbinding op te zetten met de MySQL database.
        connection = mysql.connector.connect(
            host="localhost",  # Database host
            user="root",       # Database gebruikersnaam
            password="",       # Database wachtwoord
            database="goodgarden"  # Database naam
        )

        # Controleert of de verbinding succesvol was.
        if connection.is_connected():
            return connection  # Retourneert het verbinding object.

    except Error as e:
        # Vangt en print elke fout die optreedt tijdens het verbindingsproces.
        print(f"Connection NIET gelukt! ${e}")
    
    # Retourneert None als de verbinding mislukt.
    return None
