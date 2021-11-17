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
    xhttp.send(JSON.stringify(userid));

    xhttp.onload = function () {

        let schedule = {};
        schedule = this.responseText;
        console.log(schedule);


        let t = '<tbody>'
        t += '<table>'
        t += '<tr>';
        t += '<th>Course Name</th>';
        t += '<th>Teacher</th>';
        t += '<th>Time</th>';
        t += '<th>Students Enrolled</th>';
        t += '</tr>';

        t += '<tr>';
        t += '<td>' + schedule + '</td>'


        t += '</tr>';



        t += '</table>'
        t += '</tbody>';
        document.getElementById('my-classes').innerHTML = t;


    };

}

function offeredClasses(userid) {

}