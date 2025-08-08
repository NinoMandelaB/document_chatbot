# chatbot/data_fetch.py
import sys
from os.path import dirname, abspath
from datetime import date

# Add the root directory of your project to the Python path
sys.path.append(dirname(dirname(abspath(__file__))))

from database.db_connection import create_connection

def fetch_documents():
    connection = create_connection()
    if not connection:
        return {"error": "Failed to connect to the database."}

    try:
        cursor = connection.cursor()
        query = "SELECT * FROM qualification_documents LIMIT 100;"
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()

        columns = [desc[0] for desc in cursor.description]
        documents = []
        for row in results:
            document = dict(zip(columns, row))
            # Convert date objects to strings
            for key, value in document.items():
                if isinstance(value, date):
                    document[key] = value.isoformat()
            documents.append(document)

        return {"documents": documents}
    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()
