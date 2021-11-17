INSERT INTO enrollment (id,class_id,student_id,grade)
VALUES 
(1 , 23, 5, 98),
(2, 24, 5 ,77),
(3, 10, 4, 99);

INSERT INTO classes (id,courseName,teacher_id,numberEnrolled,capacity,time)
VALUES 
(1, 'MATH 101', 'Ralph Jenkins', 4, 8, 'MWF 10:00-10:50 AM'),
(2, 'Physics 121', 'Susan Walker', 5, 10, 'TR 11:00-11:50 AM'),
(3, 'CSE 162', 'Ammon Hepworth', 4, 4, 'TR 3:00-3:50 PM'),
(4, 'CSE 106', 'Ammon Hepworth', 4, 10, 'MWF 2:00-2:50 PM');

DROP TABLE classes;
DROP TABLE enrollment;
DROP TABLE students;
DROP TABLE teachers;