function openTab(pageName) {
    var content;

    content = document.getElementsByClassName("table-content");

    for (var i = 0; i < content.length; i++) {
        content[i].style.display = "none";
    }

    document.getElementById(pageName).style.display = "block"
}

function studentClasses(userid) {
    var xhttp = new XMLHttpRequest();
    var url = "http://localhost:5000/studentView/" + userid;

    xhttp.open("GET", url, true);
    xhttp.setRequestHeader('Content-Type', 'application/json');
    xhttp.send();

    xhttp.onload = function () {

        alert('yo');

    };

}