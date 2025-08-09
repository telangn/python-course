import mysql.connector

config = {
    'user': 'root',
    'password': '37488281',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()