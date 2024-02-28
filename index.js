// your_script.js

export function executeOperation(operationChoice) {
    fetch(`/path/to/your_script.py?operation=${operationChoice}`)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            alert(data);  // You can handle the response data as needed
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
