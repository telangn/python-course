import mysql.connector

config = {
    'user': 'root',
    'password': '3******1',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()