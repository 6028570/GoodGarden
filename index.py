import mysql.connector

# Verbinding maken met de database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="goodgarden"
)

# Controleren of de verbinding succesvol is
if mydb.is_connected():
    print("Connected to the database")
else:
    print("Failed to connect to the database")

try:
    # Maak een cursor aan
    mycursor = mydb.cursor()

    # Voer de query uit om gegevens op te halen
    mycursor.execute("SELECT * FROM goodgarden.sensor_data")

    # Haal de resultaten op
    myresult = mycursor.fetchall()

    # Print de resultaten
    for x in myresult:
        print(x)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Sluit de cursor en de databaseverbinding
    mycursor.close()
    mydb.close()
