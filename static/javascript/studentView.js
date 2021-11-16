function openTab(pageName, element) {
    var content, tabs;

    content = document.getElementsByClassName("table-content");

    for (var i = 0; i < content.length; i++) {
        content[i].style.display = "none";
    }

    document.getElementById(pageName).style.display = "block"
}