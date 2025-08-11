function fetchDocuments() {
    fetch('/documents')
        .then(response => response.json())
        .then(data => {
            const documentsList = document.getElementById('documentsList');
            documentsList.innerHTML = '';

            if (data && data.length > 0) {
                // Create a table element
                let table = '<table><thead><tr>';

                // Create table headers
                const headers = Object.keys(data[0]);
                headers.forEach(header => {
                    table += `<th>${header}</th>`;
                });
                table += '</tr></thead><tbody>';

                // Create table rows
                data.forEach(doc => {
                    table += '<tr>';
                    headers.forEach(header => {
                        table += `<td>${doc[header] || ''}</td>`;
                    });
                    table += '</tr>';
                });

                table += '</tbody></table>';
                documentsList.innerHTML = table;
            } else {
                documentsList.innerHTML = '<p>No documents found.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching documents:', error);
            documentsList.innerHTML = '<p>Error fetching documents. Please try again.</p>';
        });
}


document.getElementById('chatForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const userQuery = document.getElementById('userQuery').value;

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userQuery }),
    })
    .then(response => response.json())
    .then(data => {
        const chatMessages = document.getElementById('chatMessages');
        chatMessages.innerHTML += `<p><strong>You:</strong> ${userQuery}</p>`;
        chatMessages.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
        document.getElementById('userQuery').value = '';
    })
    .catch(error => console.error('Error chatting:', error));
});
