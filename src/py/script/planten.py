import json
import mysql.connector
import os

# Function to make a connection to the database
def database_connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="goodgarden"
    )

# Function to get the absolute path of the current directory
def get_current_directory():
    return os.path.dirname(os.path.abspath(__file__))

def fetch_plant_and_write_to_json():
    # Establish a database connection
    connection = database_connect()
    
    try:
        cursor = connection.cursor(dictionary=True)  # To fetch rows as dictionaries
        # Execute the query to fetch data
        cursor.execute("SELECT id, plant_naam, plantensoort, plant_geteelt FROM planten")
        # Fetch all rows
        plants = cursor.fetchall()
        
        # Get the absolute path of the current directory
        current_directory = get_current_directory()
        # Construct the absolute path for the JSON file
        json_file_path = os.path.join(current_directory, 'plants.json')
        
        # Write fetched data to JSON file
        with open(json_file_path, 'w') as json_file:
            json.dump(plants, json_file, indent=4)
            
    except mysql.connector.Error as error:
        print("Error fetching data from MySQL table:", error)
        
    finally:
        # Close cursor and connection
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()

# Call the function to fetch data and write to JSON
fetch_plant_and_write_to_json()
