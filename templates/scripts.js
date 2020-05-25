// execute the function when the user scrolls the page

window.onscroll = function() {scrollFunction()};

// Get navbar
var navbar = document.getElementById("navbar");

// Get offset position of the navbar

var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when scroll position is reached
// Remove sticky when scroll position is left

function scrollFunction(){
    if (window.pageYOffset >= sticky){
        navbar.classList.add("sticky")
    }
    else{
        navbar.classList.remove("sticky");
    }
}