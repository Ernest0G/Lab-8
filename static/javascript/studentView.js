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

        let schedule = {};
        schedule = this.responseText;
        console.log(schedule);
        let scheduleParsed = JSON.parse(schedule);

        console.log(scheduleParsed);

        let t = '<tbody>'
        t += '<tr>';
        t += '<th>Course Name</th>';
        t += '<th>Teacher</th>';
        t += '<th>Time</th>';
        t += '<th>Students Enrolled</th>';
        t += '</tr>';
        for (item in scheduleParsed) {

            console.log(item)

        }
        t += '<tr>';
        t += '<td>' + key + '</td>';
        t += '<td>' + value + '</td>';
        t += '</tr>';
        t += '</tbody>';
        document.getElementById('my-classes').innerHTML = t;


    };

}

function addCourse(params) {

}