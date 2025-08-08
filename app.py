# app.py
from flask import Flask, jsonify, request
from database.db_connection import create_connection, execute_read_query
from sql_queries.queries import get_documents_query
from chatbot.chatbot_service import process_query

app = Flask(__name__)

@app.route('/documents', methods=['GET'])
def get_documents():
    connection = create_connection()
    if connection:
        # Pass the connection to get_documents_query
        documents = get_documents_query(connection)
        connection.close()
        return jsonify(documents)
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

@app.route('/documents', methods=['POST'])
def add_document():
    document_data = request.json
    connection = create_connection()
    if connection:
        insert_document_query(connection, document_data)
        connection.close()
        return jsonify({"message": "Document added successfully"}), 201
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query')
    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    response = process_query(user_query)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
