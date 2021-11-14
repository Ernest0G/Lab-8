from server import Users,db

Jose = Users(id = 1, username='JSantos', password='Jsantos123') 
db.session.add(Jose) 

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