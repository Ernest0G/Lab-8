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
    var url = "http://localhost:5000/studentView/myClasses/" + userid;

    xhttp.open("GET", url, true);
    xhttp.send(JSON.stringify(userid));

    xhttp.onload = function () {

        let schedule = this.responseText;
        let scheduleParsed = JSON.parse(schedule)
        console.log(scheduleParsed);

        let t = '<tbody>'
        t += '<table>'
        t += '<tr>';
        t += '<th>Course Name</th>';
        t += '<th>Teacher</th>';
        t += '<th>Time</th>';
        t += '<th>Students Enrolled</th>';
        t += '</tr>';


        for (i in scheduleParsed) {
            t += '<tr>';

            t += '<td>' + scheduleParsed[i] + '</td>';


            t += '</tr>';
        }






        t += '</table>'
        t += '</tbody>';
        document.getElementById('my-classes').innerHTML = t;


    };

}

function offeredClasses(userid) {
    var xhttp = new XMLHttpRequest();
    var url = "http://localhost:5000/studentView/offeredCourses/" + userid;

    xhttp.open("GET", url, true);
    xhttp.send(JSON.stringify(userid));

    xhttp.onload = function () {

        let schedule = [];
        schedule = this.responseText;
        let scheduleParsed = JSON.parse(schedule)
        console.log(scheduleParsed);

        let t = '<tbody>'
        t += '<table>'
        t += '<tr>';
        t += '<th>Course Name</th>';
        t += '<th>Teacher</th>';
        t += '<th>Time</th>';
        t += '<th>Students Enrolled</th>';
        t += '<th>Add Class</th>';
        t += '</tr>';


        for (i in scheduleParsed) {
            t += '<tr>';

            t += '<td>' + scheduleParsed[i] + '</td>';


            t += '</tr>';
        }






        t += '</table>'
        t += '</tbody>';
        document.getElementById('offered-courses').innerHTML = t;


    };
}