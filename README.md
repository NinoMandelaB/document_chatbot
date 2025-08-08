# Document Status Bot

A Flask-based application designed to manage and query documents stored in a PostgreSQL database. The application also includes a chatbot service to process user queries related to the documents.

## Project Structure

```
.
├── chatbot/
│   └── chatbot_service.py
├── database/
│   └── db_connection.py
├── sql_queries/
│   └── queries.py
├── .gitignore
├── Procfile
├── app.py
└── requirements.txt
```

## Setup Instructions

### Prerequisites

- Python 3.12.4
- PostgreSQL
- Flask
- Additional dependencies listed in `requirements.txt`

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd my_project
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory and add your environment-specific variables:
     ```
     DB_HOST=your_postgres_host
     DB_NAME=your_database_name
     DB_USER=your_database_user
     DB_PASSWORD=your_database_password
     DB_PORT=your_database_port
     MISTRAL_API_KEY=your_mistral_api_key
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

## API Endpoints

- **GET /documents**: Retrieve all documents from the database.
- **POST /documents**: Add a new document to the database.
- **POST /chat**: Process a user query using the chatbot service.

## Usage

- **Retrieve Documents**: Send a GET request to `/documents` to fetch all documents.
- **Add a Document**: Send a POST request to `/documents` with the document data in JSON format.
- **Chat with the Bot**: Send a POST request to `/chat` with a JSON payload containing the user query.

## Deployment

To deploy the application on platforms like Railway:

1. **Set Up Environment Variables**: Configure the necessary environment variables in the Railway dashboard.
2. **Deploy**: Push your code to the connected GitHub repository, and Railway will automatically deploy the application.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
```

### Additional Tips

- **Customization**: Feel free to add more sections or details specific to your project, such as configuration instructions, example requests, or additional setup steps.
- **Images**: If you have any diagrams or screenshots that could help users understand the project better, consider adding them to the `README.md`.
- **Badges**: You can also add badges for build status, coverage, etc., if you are using any CI/CD tools.
