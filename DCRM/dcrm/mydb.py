import mysql.connector

def create_database():
    try:
        # Connect to MySQL server (change username and password as needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Coding2$tks"
        )

        # Create cursor object
        cursor = connection.cursor()

        # Execute SQL query to create database
        cursor.execute("CREATE DATABASE my_db")

        print("Database 'my_db' created successfully.")

    except mysql.connector.Error as error:
        print(f"Failed to create database: {error}")


if __name__ == "__main__":
    create_database()
