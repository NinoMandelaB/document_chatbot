from flask import Flask, jsonify, request, render_template
from database.db_connection import create_connection
from sql_queries.queries import get_documents_query, insert_document_query, update_document_query
from chatbot.chatbot_service import process_query

app = Flask(__name__)

@app.route('/documents', methods=['GET'])
def get_documents():
    connection = create_connection()
    if connection:
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

@app.route('/documents/<int:document_id>', methods=['PUT'])
def update_document(document_id):
    document_data = request.json
    connection = create_connection()
    if connection:
        update_document_query(connection, document_id, document_data)
        connection.close()
        return jsonify({"message": "Document updated successfully"}), 200
    else:
        return jsonify({"error": "Failed to connect to the database"}), 500

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('query')
    if not user_query:
        return jsonify({"error": "No query provided"}), 400
    response = process_query(user_query)
    return jsonify(response)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
