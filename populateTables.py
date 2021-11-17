from server import Users, Students, Teachers, Classes, Enrollment, db
db.drop_all()
db.create_all() 


#User Info
Jose = Users(id = 1, username='JSantos', password='JSantos123', userLevel=0)
Betty = Users(id = 2,username='BBrown', password='BBrown123', userLevel=0) 
John = Users(id = 3,username='JStuart', password='JStuart123', userLevel=0)
Li = Users(id = 4,username='LCheng', password='LCheng123', userLevel=0)
Nancy = Users(id = 5,username='NLittle',password= 'NLittle123', userLevel=0)
Mindy = Users(id = 6,username='MNorris',password= 'MNorris123', userLevel=0)
Aditya = Users(id = 7,username='ARanganath',password= 'ARanganath123', userLevel=0)
Yi = Users(id = 8,username='YChen',password= 'YChen123', userLevel=0)

db.session.add(Jose) 
db.session.add(Betty) 
db.session.add(John) 
db.session.add(Li) 
db.session.add(Nancy) 
db.session.add(Mindy) 
db.session.add(Aditya) 
db.session.add(Yi)

Ralph = Users(id = 9,username='RJenkins',password= 'RJenkins123', userLevel=1)
Susan = Users(id = 10,username='SWalker',password= 'SWalker123', userLevel=1)
Ammon = Users(id = 11,username='AHepworth',password= 'AHepworth123', userLevel=1)
admin = Users(id = 12,username="admin",password="password", userLevel=2)
db.session.add(Ralph)
db.session.add(Susan)
db.session.add(Ammon)
db.session.add(admin)

db.session.flush()

#Student Info
Jose_student = Students(id=1, name="Jose Santos", user_id=Jose.id)
Betty_student = Students(id=2, name="Betty Brown", user_id=Betty.id)
John_student = Students(id=3, name="John Stuart", user_id=John.id)
Li_student = Students(id=4, name="Li Cheng", user_id=Li.id)
Nancy_student = Students(id=5, name="Nancy Little", user_id=Nancy.id)
Mindy_student = Students(id=6, name="Mindy Norris", user_id=Mindy.id)
Aditya_student = Students(id=7, name="Aditya Ranganath", user_id=Aditya.id)
Yi_student = Students(id=8, name="Yi Wen Chen", user_id=Yi.id)
db.session.add(Jose_student) 
db.session.add(Betty_student) 
db.session.add(John_student) 
db.session.add(Li_student) 
db.session.add(Nancy_student) 
db.session.add(Mindy_student) 
db.session.add(Aditya_student) 
db.session.add(Yi_student)

#Teacher Info
Ralph_teacher = Teachers(id=1, name='Ralph Jenkins', user_id=Ralph.id)
Susan_teacher = Teachers(id=2, name='Susan Walker', user_id=Susan.id)
Ammon_teacher = Teachers(id=3, name='Ammon Hepworth', user_id=Ammon.id)
db.session.add(Ralph_teacher)
db.session.add(Susan_teacher)
db.session.add(Ammon_teacher)

db.session.flush()

#Class info
math101 = Classes(id=1, courseName='Math 101', teacher_id = Ralph_teacher.id,
    numberEnrolled = 4, 
    capacity = 8,
    time = 'MWF 10:00-10:50am')

physics121 = Classes(id=2, courseName='Physics 101', teacher_id = Susan_teacher.id,
    numberEnrolled = 5, 
    capacity = 10,
    time = 'TR 11:00-11:50am')

cs106 = Classes(id=3, courseName='CS 101', teacher_id = Ammon_teacher.id,
    numberEnrolled = 4, 
    capacity = 10,
    time = 'MWF 2:00-2:50pm')

cs162 = Classes(id=4, courseName='CS 162', teacher_id = Ammon_teacher.id,
    numberEnrolled = 4, 
    capacity = 4,
    time = 'TR 3:00-3:50pm')

db.session.add(math101)
db.session.add(physics121)
db.session.add(cs106)
db.session.add(cs162)

db.session.flush()

#Enrollment Info
db.session.add(Enrollment(id=1, class_id=math101.id, student_id=Jose_student.id, grade=92))
db.session.add(Enrollment(id=2, class_id=math101.id, student_id=Betty_student.id, grade=65))
db.session.add(Enrollment(id=3, class_id=math101.id, student_id=John_student.id, grade=86))
db.session.add(Enrollment(id=4, class_id=math101.id, student_id=Li_student.id, grade=77))

db.session.add(Enrollment(id=5, class_id=physics121.id, student_id=Nancy_student.id, grade=53))
db.session.add(Enrollment(id=6, class_id=physics121.id, student_id=Li_student.id, grade=85))
db.session.add(Enrollment(id=7, class_id=physics121.id, student_id=Mindy_student.id, grade=94))
db.session.add(Enrollment(id=8, class_id=physics121.id, student_id=John_student.id, grade=91))
db.session.add(Enrollment(id=9, class_id=physics121.id, student_id=Betty_student.id, grade=88))

db.session.add(Enrollment(id=10, class_id=cs106.id, student_id=Aditya_student.id, grade=93))
db.session.add(Enrollment(id=11, class_id=cs106.id, student_id=Yi_student.id, grade=85))
db.session.add(Enrollment(id=12, class_id=cs106.id, student_id=Nancy_student.id, grade=57))
db.session.add(Enrollment(id=13, class_id=cs106.id, student_id=Mindy_student.id, grade=68))

db.session.add(Enrollment(id=14, class_id=cs162.id, student_id=Aditya_student.id, grade=99))
db.session.add(Enrollment(id=15, class_id=cs162.id, student_id=Nancy_student.id, grade=87))
db.session.add(Enrollment(id=16, class_id=cs162.id, student_id=Yi_student.id, grade=92))
db.session.add(Enrollment(id=17, class_id=cs162.id, student_id=John_student.id, grade=67))


db.session.commit()