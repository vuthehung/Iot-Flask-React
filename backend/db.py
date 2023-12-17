from flask_mysqldb import MySQL
from flask import current_app
from datetime import datetime

mysql = MySQL()

def init_db(app):
    mysql.init_app(app)

def save_video_info(ten):
    try:
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO videos (ten, created_at) VALUES (%s, %s)", (ten, datetime.now()))
        mysql.connection.commit()
        cur.close()
        return True
    except Exception as e:
        print(f"Error saving video info to database: {e}")
        return False