let myButton = document.getElementById("btn-back-to-top");

window.onscroll = function() {
    scrollFunction();
}

function scrollFunction() {
    if (document.body.scrollTop > 5 || document.documentElement.scrollTop > 5) {
        myButton.style.display = "block";
    } else {
        myButton.style.display = "none";
    }
}

myButton.addEventListener("click", backToTop);

function backToTop() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}