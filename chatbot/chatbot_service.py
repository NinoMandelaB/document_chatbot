import requests
from .data_fetch import fetch_documents
import json
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

def query_mistral_api(user_query, documents=None):
    api_url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.getenv('MISTRAL_API_KEY')}",  # Fetch the API key from environment variables
        "Content-Type": "application/json"
    }

    current_date = datetime.now().strftime("%Y-%m-%d")

    if documents:
        system_prompt = f"""
        You are an assistant that helps answer questions about documents.
        Today's date is {current_date}.

        Here are the documents in JSON format: {json.dumps(documents, indent=2)}.

        Document Structure:
        - document_id: Unique identifier for the document.
        - type_of_document: Type of document (e.g., RA, DQ, QP).
        - document_link: URL to access the document.
        - draft_due_date, draft_actual_date: Draft dates.
        - system_owner_review_due_date, system_owner_review_actual_date: Review dates.
        - qa_review_due_date, qa_review_actual_date: QA review dates.
        - master_control_release_due_date, master_control_release_actual_date: Release dates.
        - status: Current status of the document.
        - qualification_engineer, system_owner, qa_responsible: People involved.
        - system_name: Name of the system (e.g., N2-Distribution).

        Instructions:
        - Understand and respond to questions about documents that could be based on fields like 'type_of_document', 'system_name', 'qa_responsible', 'draft_due_date', etc.
        - If a user asks questions like, 'Which document is Jens Mantwill responsible for?' or 'What document is due this week?', interpret these questions to filter and respond with relevant information from the documents.
        - Use the information in the relevant documents to answer the user's question accurately.
        - Combine information from multiple documents if necessary to provide a complete answer.
        - If information is missing or unclear, provide a reasoned response based on available data.
        """
    else:
        system_prompt = f"""
        You are an assistant that helps answer questions about documents.
        Today's date is {current_date}.

        If the user asks about the status or details of qualification or validation documents, respond with 'fetching the documents'.
        Otherwise, respond naturally to the query.
        """

    data = {
        "model": "mistral-small",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_query}
        ]
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while querying the API: {e}")
        return None

def process_query(query):
    print(f"Processing query: {query}")
    result = query_mistral_api(query)

    if result and "choices" in result and len(result["choices"]) > 0:
        response_text = result["choices"][0]["message"]["content"].strip()
        print(f"Model initial response: {response_text}")

        if "fetching the documents" in response_text.lower():
            print("Fetching documents...")
            document_data = fetch_documents()

            if "error" in document_data:
                return {"response": f"An error occurred: {document_data['error']}"}
            else:
                documents = document_data.get('documents', [])
                print(f"Fetched documents count: {len(documents)}")

                if documents:
                    print("Documents fetched:", json.dumps(documents, indent=2))
                    summary_result = query_mistral_api(query, documents)

                    if summary_result and "choices" in summary_result and len(summary_result["choices"]) > 0:
                        summary_text = summary_result["choices"][0]["message"]["content"].strip()
                        return {"response": summary_text}
                    else:
                        return {"response": "I couldn't generate a summary for the documents."}
                else:
                    return {"response": "No documents found."}
        else:
            return {"response": response_text}
    else:
        return {"response": "I couldn't generate a valid response."}
