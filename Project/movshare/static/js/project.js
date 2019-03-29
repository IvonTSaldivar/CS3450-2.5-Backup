/* Project specific Javascript goes here. */

function toggleHideContent(var id){
    var content = document.getElementById(id);
    if(content)
        if(content.style.display == "hidden"){
            content.style.display = "block";
        } else if (content.style.display == "block"){
            content.style.display = "hidden";
        }
    }
}

function toggleButton(var id){
    toggleHideContent(id);
    toggleOtherButton(id);
}
function toggleOtherButton(var id){
    var otherID;
    if (id == "addMediaButton"){
        otherID = "addShelfButton";
    } else otherID = "addMediaButton";
    var button = document.getElementById(otherID);
    button.style.display = "hidden";
}
