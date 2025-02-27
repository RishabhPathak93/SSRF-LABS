document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("ssrf-form");
    form.addEventListener("submit", (event) => {
        const urlInput = document.getElementById("url-input").value;
        if (!urlInput.startsWith("http://") && !urlInput.startsWith("https://")) {
            event.preventDefault();
            alert("Invalid URL. Please enter a valid URL starting with http:// or https://");
        }
    });
});