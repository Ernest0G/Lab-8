function openTab(pageName) {
    var content;

    content = document.getElementsByClassName("table-content");

    for (var i = 0; i < content.length; i++) {
        content[i].style.display = "none";
    }

    document.getElementById(pageName).style.display = "block"
}