const form = document.getElementById('urlForm');
const input = document.getElementById('urlInput');

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
})