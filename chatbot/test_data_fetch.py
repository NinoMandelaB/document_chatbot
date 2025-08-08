# test_data_fetch.py
from .data_fetch import fetch_documents

def test_fetch_documents():
    # Call the fetch_documents function
    result = fetch_documents()

    # Check if the result contains an error
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        # Print the fetched documents
        print("Fetched Documents:")
        for document in result["documents"]:
            print(document)

if __name__ == "__main__":
    test_fetch_documents()
