import mysql.connector #** TYPE IN TERMINAL: "pip install mysql-connector-python"
from mysql.connector import Error

def database_connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="goodgarden"
        )
        if connection.is_connected():
            # print("Connection gelukt!")
            return connection
    except Error as e:
        print(f"Connection NIET gelukt! ${e}")
    return None

# database_connect()