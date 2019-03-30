/* Project specific Javascript goes here. */

function toggleHideContent(id){
    var content = document.getElementById(id);
    if(content){
        if(content.style.display == "none"){
            content.style.display = "block";
        } else if (content.style.display == "block"){
            content.style.display = "none";
        }
    }
}

function toggleButton(id){
    toggleHideContent(id);
    toggleOtherButton(id);
}

function toggleOtherButton(id){
    var otherID;
    if (id == "addMediaBlock"){
        otherID = "addShelfBlock";
    } else otherID = "addMediaBlock";
    var button = document.getElementById(otherID);
    button.style.display = "none";
}
