from server import Users,db

#User Info
Jose = Users(id = 1, username='JSantos', password='JSantos123')
Betty = Users(id = 2,username='BBrown', password='BBrown123') 
John = Users(id = 3,username='JStuart', password='JStuart123')
Li = Users(id = 4,username='LCheng', password='LCheng123')
Nancy = Users(id = 5,username='NLittle',password= 'NLittle123')
Mindy = Users(id = 6,username='MNorris',password= 'MNorris123')
Aditya = Users(id = 7,username='ARanganath',password= 'ARanganath123')
Yi = Users(id = 8,username='YChen',password= 'YChen123')

db.session.add(Jose) 
db.session.add(Betty) 
db.session.add(John) 
db.session.add(Li) 
db.session.add(Nancy) 
db.session.add(Mindy) 
db.session.add(Aditya) 
db.session.add(Yi)

Ralph = Users(id = 9,username='RJenkins',password= 'RJenkins123')
Susan = Users(id = 10,username='SWalker',password= 'SWalker123')
Ammon = Users(id = 11,username='AHepworth',password= 'AHepworth123')
admin = Users(id = 12,username="admin",password="password")
db.session.add(Ralph)
db.session.add(Susan)
db.session.add(Ammon)
db.session.add(admin)

#Student Info
Jose_student = Students(id=1, name="Jose Santos", user=Jose)
Betty_student = Students(id=2, name="Betty Brown", user=Betty)
John_student = Students(id=3, name="John Stuart", user=John)
Li_student = Students(id=4, name="Li Cheng", user=Li)
Nancy_student = Students(id=5, name="Nancy Little", user=Nancy)
Mindy_student = Students(id=6, name="Mindy Norris", user=Mindy)
Aditya_student = Students(id=7, name="Aditya Ranganath", user=Aditya)
Yi_student = Students(id=8, name="Yi Wen Chen", user=Yi)
db.session.add(Jose_student) 
db.session.add(Betty_student) 
db.session.add(John_student) 
db.session.add(Li_student) 
db.session.add(Nancy_student) 
db.session.add(Mindy_student) 
db.session.add(Aditya_student) 
db.session.add(Yi_student)

#Teacher Info
Ralph_teacher = Teachers(id=1, name='Ralph Jenkins', user=Ralph)
Susan_teacher = Teachers(id=2, name='Susan Walker', user=Susan)
Ammon_teacher = Teachers(id=3, name='Ammon Hepworth', user=Ammon)
db.session.add(Ralph_teacher)
db.session.add(Susan_teacher)
db.session.add(Ammon_teacher)

#Class info
math101 = Classes(id=1, courseName='Math 101', teacher = Ralph_teacher,
    numberEnrolled = 4, 
    capacity = 8,
    time = 'MWF 10:00-10:50am')

physics121 = Classes(id=2, courseName='Physics 101', teacher = Susan_teacher,
    numberEnrolled = 5, 
    capacity = 10,
    time = 'TR 11:00-11:50am')

cs106 = Classes(id=3, courseName='CS 101', teacher = Ammon_teacher,
    numberEnrolled = 4, 
    capacity = 10,
    time = 'MWF 2:00-2:50pm')

cs162 = Classes(id=4, courseName='CS 162', teacher = Ammon_teacher,
    numberEnrolled = 4, 
    capacity = 4,
    time = 'TR 3:00-3:50pm')

db.session.add(math101)
db.session.add(physics121)
db.session.add(cs106)
db.session.add(cs162)

#Enrollment Info
db.session.add(Enrollment(id=1, classes=math101, student=Jose_student, grade=92))
db.session.add(Enrollment(id=2, classes=math101, student=Betty_student, grade=65))
db.session.add(Enrollment(id=3, classes=math101, student=John_student, grade=86))
db.session.add(Enrollment(id=4, classes=math101, student=Li_student, grade=77))

db.session.add(Enrollment(id=5, classes=physics121, student=Nancy_student, grade=53))
db.session.add(Enrollment(id=6, classes=physics121, student=Li_student, grade=85))
db.session.add(Enrollment(id=7, classes=physics121, student=Mindy_student, grade=94))
db.session.add(Enrollment(id=8, classes=physics121, student=John_student, grade=91))
db.session.add(Enrollment(id=9, classes=physics121, student=Betty_student, grade=88))

db.session.add(Enrollment(id=10, classes=cs106, student=Aditya_student, grade=93))
db.session.add(Enrollment(id=11, classes=cs106, student=Yi_student, grade=85))
db.session.add(Enrollment(id=12, classes=cs106, student=Nancy_student, grade=57))
db.session.add(Enrollment(id=13, classes=cs106, student=Mindy_student, grade=68))

db.session.add(Enrollment(id=14, classes=cs162, student=Aditya_student, grade=99))
db.session.add(Enrollment(id=15, classes=cs162, student=Nancy_student, grade=87))
db.session.add(Enrollment(id=16, classes=cs162, student=Yi_student, grade=92))
db.session.add(Enrollment(id=17, classes=cs162, student=John_student, grade=67))


db.session.commit()