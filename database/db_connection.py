# database/db_connection.py
import psycopg2
from psycopg2 import OperationalError

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            host='trolley.proxy.rlwy.net',
             database='postgres',
            user='postgres',
            password='veKMIWZDjeHSkYnwvIOoXLdbklciVvUX',
            port='45530'
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


