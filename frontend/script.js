const form = document.getElementById('urlForm');
const input = document.getElementById('urlInput');
const summaryOutput = document.getElementById('summaryBox');


function isValidUrl(url) {
    try {
        new URL(url)
        return true
    }catch (e) {
        return false;
    }
}

form.addEventListener('submit', function(event) {
    event.preventDefault(); 
    const url = input.value.trim();
    console.log("User entered:", url);  

    if (!url) {
        alert('Please enter a URL.');
        return;
    }
    if (!isValidUrl (url)) {
        alert('Please enter a valid URL.');
        return;
    }
    const data = {url : url};
    fetch("http://localhost:8000/summarize",{
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Server returned an error');    
        }
        return response.json();
    })
    . then (data => {
        console.log ("Summary received:", data.summary);
        summaryOutput.textContent = data.summary;
    })
    .catch(error => {
        console.error('Fetch error:',error);
        alert('An error occurred while fetching the summary. Please try again later.');
    });
});