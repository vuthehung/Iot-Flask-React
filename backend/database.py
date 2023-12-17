import mysql.connector
from mysql.connector import Error
from datetime import datetime

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='1',
            database='iot'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def insert_video_record(connection, video_path, datetime_detect):
    try:
        cursor = connection.cursor()
        query = "INSERT INTO videos (path, datetime_detect) VALUES (%s, %s)"
        values = (video_path, datetime_detect)
        cursor.execute(query, values)
        connection.commit()
        print("Video record inserted successfully")
    except Error as e:
        print(f"Error: {e}")

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Connection to MySQL database closed")
