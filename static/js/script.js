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


function handleFormSubmit() {
    togglePreloader(true); 

    
    setTimeout(() => {
        togglePreloader(false); 
    }, 3000); 
}


document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("scrapeForm");
    form.addEventListener("submit", function(event) {
        event.preventDefault();
        handleFormSubmit();
    });
});
