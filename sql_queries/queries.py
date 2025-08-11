def get_documents_query(connection):
    query = "SELECT * FROM qualification_documents;"
    cursor = connection.cursor()
    cursor.execute(query)
    # Fetch column names from cursor description
    column_names = [desc[0] for desc in cursor.description]
    # Fetch all rows from the executed query
    results = cursor.fetchall()
    cursor.close()
    # Return column names and results
    return column_names, results


def insert_document_query(connection, document_data):
    # Define the SQL query using placeholders
    query = """
    INSERT INTO qualification_documents (
        type_of_document, document_link, draft_due_date, draft_actual_date,
        system_owner_review_due_date, system_owner_review_actual_date,
        qa_review_due_date, qa_review_actual_date,
        master_control_release_due_date, master_control_release_actual_date,
        status, qualification_engineer, system_owner, qa_responsible, system_name
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s
    );
    """
    # Convert empty dates to None
    def date_or_none(date_str):
        return date_str if date_str else None

    # Prepare data with conversion of empty strings to None for dates
    data = (
        document_data['type_of_document'], document_data['document_link'],
        date_or_none(document_data.get('draft_due_date', '')),
        date_or_none(document_data.get('draft_actual_date', '')),
        date_or_none(document_data.get('system_owner_review_due_date', '')),
        date_or_none(document_data.get('system_owner_review_actual_date', '')),
        date_or_none(document_data.get('qa_review_due_date', '')),
        date_or_none(document_data.get('qa_review_actual_date', '')),
        date_or_none(document_data.get('master_control_release_due_date', '')),
        date_or_none(document_data.get('master_control_release_actual_date', '')),
        document_data['status'], document_data['qualification_engineer'],
        document_data['system_owner'], document_data['qa_responsible'], document_data['system_name']
    )

    # Execute the query with the data tuple
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    cursor.close()

def update_document_query(connection, document_id, document_data):
    query = """
    UPDATE qualification_documents
    SET
        type_of_document = %s,
        document_link = %s,
        draft_due_date = %s,
        draft_actual_date = %s,
        system_owner_review_due_date = %s,
        system_owner_review_actual_date = %s,
        qa_review_due_date = %s,
        qa_review_actual_date = %s,
        master_control_release_due_date = %s,
        master_control_release_actual_date = %s,
        status = %s,
        qualification_engineer = %s,
        system_owner = %s,
        qa_responsible = %s,
        system_name = %s
    WHERE id = %s;
    """

    # Convert empty dates to None
    def date_or_none(date_str):
        return date_str if date_str else None

    # Prepare data with conversion of empty strings to None for dates
    data = (
        document_data['type_of_document'],
        document_data['document_link'],
        date_or_none(document_data.get('draft_due_date', '')),
        date_or_none(document_data.get('draft_actual_date', '')),
        date_or_none(document_data.get('system_owner_review_due_date', '')),
        date_or_none(document_data.get('system_owner_review_actual_date', '')),
        date_or_none(document_data.get('qa_review_due_date', '')),
        date_or_none(document_data.get('qa_review_actual_date', '')),
        date_or_none(document_data.get('master_control_release_due_date', '')),
        date_or_none(document_data.get('master_control_release_actual_date', '')),
        document_data['status'],
        document_data['qualification_engineer'],
        document_data['system_owner'],
        document_data['qa_responsible'],
        document_data['system_name'],
        document_id
    )

    # Execute the query with the data tuple
    cursor = connection.cursor()
    cursor.execute(query, data)
    connection.commit()
    cursor.close()
