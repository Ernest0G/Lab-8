<<<<<<< Updated upstream
from server import Users,db
=======
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
>>>>>>> Stashed changes

Jose = Users(id = 1, username='JSantos', password='Jsantos123') 
db.session.add(Jose) 
<<<<<<< Updated upstream
=======
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
>>>>>>> Stashed changes

Betty = Users(id = 2,username='BBrown', password='BBrown123') 
db.session.add(Betty) 

John = Users(id = 3,username='JStuart', password='JStuart123') 
db.session.add(John) 

Li = Users(id = 4,username='LCheng', password='LCheng123') 
db.session.add(Li) 

Nancy = Users(id = 5,username='NLittle',password= 'NLittle123') 
db.session.add(Nancy) 

Mindy = Users(id = 6,username='MNorris',password= 'MNorris123') 
db.session.add(Mindy) 

Aditya = Users(id = 7,username='ARanganath',password= 'ARanganath123') 
db.session.add(Aditya) 

Yi = Users(id = 8,username='YChen',password= 'YChen123') 
db.session.add(Yi) 

db.session.commit() 
