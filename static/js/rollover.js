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
    img.base_url = img.src;
    (new Image()).src = img.rollover_url = rollover_url;
}

function make_images_changer(images, property) {
    return function () {
        for ( var j = 0; j < images.length; j++ ) {
            images[j].src = images[j][property];
        }
    }
}

function init_rollovers() {
    var images = document.getElementsByTagName("img");
    for ( var i = 0; i < images.length; i++ ) {
        var image = images[i];
        var rollover_url = image.getAttribute("rollover");
        if ( rollover_url )
            add_rollover(image, rollover_url);
    }
    
    var objs = {};
    var links = document.getElementsByTagName("a");
    for ( var i = 0; i < links.length; i++ ) {
        var href = links[i].href;
        if ( href ) {
            var child = links[i].children[0];
            if ( child && child.tagName.toLowerCase() == "img" &&
                 child.getAttribute("rollover") ) {
                if ( objs[href] )
                    objs[href].push(child);
                else
                    objs[href] = [child];
            }
        }
    }

    for ( var href in objs ) {
        for ( var i = 0; i < objs[href].length; i++ ) {
            with ( objs[href][i] ) {
                onmouseover = make_images_changer(objs[href], "rollover_url");
                onmouseout = make_images_changer(objs[href], "base_url");
            }
        }
    }
}

if ( window.addEventListener )
    window.addEventListener("load", init_rollovers, false);
else if ( window.attachEvent )
    window.attachEvent("onload", init_rollovers);
