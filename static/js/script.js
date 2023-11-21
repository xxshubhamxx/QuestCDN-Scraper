function preloader(){
    document.getElementById("loading").style.display = "none";
    document.getElementById("content").style.display = "block";
}
window.onload = preloader;

function toggleLoading() {
    document.getElementById("loading").style.display = "block";
    document.getElementById("content").style.display = "none";
}

function toggleContent() {
    document.getElementById("loading").style.display = "none";
    document.getElementById("content").style.display = "block";
}

/* static/js/script.js */

// Function to show/hide preloader and content
function togglePreloader(show) {
    const preloader = document.getElementById("loading");
    const content = document.getElementById("content");

    if (show) {
        preloader.style.display = "flex";
        content.style.display = "none";
    } else {
        preloader.style.display = "none";
        content.style.display = "block";
    }
}

// Function to handle form submission
function handleFormSubmit() {
    togglePreloader(true); // Show preloader on form submit

    // Add a slight delay to mimic processing (remove this in actual usage)
    setTimeout(() => {
        togglePreloader(false); // Hide preloader after some delay (for demo)
    }, 3000); // Change delay time as needed or replace with actual functionality
}

// Event listener for form submission
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("scrapeForm");
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        handleFormSubmit();
    });
});
