import mysql.connector

def connect(database):

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Your database password",
        database=database
    )

    return connection
