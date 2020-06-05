upButton = document.getElementById("topButton"); // create button object

window.onsroll = function(){
    scrollFunction();
}

function scrollFunction(){
    if(document.body.scrollTop > 20 || document.documentElement.scrollTop > 20){
        upButton.style.display = "block"
    }
    else{
        upButton.style.display = "none"
    }
}

function topFunction(){
    document.body.scrollTop{
        document.body.scrollTop = 0; // for safari users
        document.documentElement.scrollTop = 0; // for chrome, firefox, IE and opera users

    }
}