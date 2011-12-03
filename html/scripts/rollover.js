function add_rollover(img, rollover_url) {
    if (typeof img == "string") {
        var id = img;
        img = null;

        if ( document.getElementById )
            img = document.getElementById(id);
        else if ( document.all ) img = document.all[id];

        if ( !img ) img = document.images[id];
        if ( !img ) return;
    }

    if ( img.tagName.toLowerCase() != "img" ) return;
    var base_url = img.src;
    (new Image()).src = rollover_url;

    img.onmouseover = function() { img.src = rollover_url; }
    img.onmouseout = function() { img.src = base_url; }
}

function init_rollovers() {
    var images = document.getElementsByTagName("img");
    for ( var i = 0; i < images.length; i++ ) {
        var image = images[i];
        var rollover_url = image.getAttribute("rollover");
        if ( rollover_url )
            add_rollover(image, rollover_url);
    }
}

if ( window.addEventListener )
    window.addEventListener("load", init_rollovers, false);
else if ( window.attachEvent )
    window.attachEvent("onload", init_rollovers);
