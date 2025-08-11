function fetchDocuments() {
    fetch('/documents')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            const documentsList = document.getElementById('documentsList');
            documentsList.innerHTML = '';

            if (data && data.column_names && data.results && data.results.length > 0) {
                // Create a table element
                let table = document.createElement('table');

                // Create table header
                let thead = document.createElement('thead');
                let headerRow = document.createElement('tr');

                // Create table headers using column names
                data.column_names.forEach(header => {
                    let th = document.createElement('th');
                    th.textContent = header;
                    headerRow.appendChild(th);
                });

                thead.appendChild(headerRow);
                table.appendChild(thead);

                // Create table body
                let tbody = document.createElement('tbody');

                // Create table rows
                data.results.forEach(row => {
                    let tr = document.createElement('tr');
                    row.forEach(cell => {
                        let td = document.createElement('td');
                        td.textContent = cell || '';
                        tr.appendChild(td);
                    });
                    tbody.appendChild(tr);
                });

                table.appendChild(tbody);
                documentsList.appendChild(table);
            } else {
                documentsList.innerHTML = '<p>No documents found.</p>';
            }
        })
        .catch(error => {
            console.error('Error fetching documents:', error);
            documentsList.innerHTML = '<p>Error fetching documents. Please try again.</p>';
        });
}

// Call fetchDocuments when the page loads
window.onload = fetchDocuments;



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
