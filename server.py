from enum import unique
from html import entities
from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
from flask_login import current_user, login_user, LoginManager, UserMixin, logout_user
from flask_admin import Admin
from sqlalchemy.sql.elements import Null

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.sqlite"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'secret-key'
admin = Admin(app)

class Users(UserMixin,db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String, unique=True, nullable=False) 
    password = db.Column(db.String, unique=False, nullable=False)
    userLevel = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self): 
        return '<Users %r>' % self.username

    def checkPassword(self,password):
        return self.password == password

class Students(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=False, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True,nullable=False)
    
    user = db.relationship('Users',backref=db.backref('student',lazy=True ))

    def __repr__(self): 
        return '<Students %r>' % self.name

class Enrollment(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'),unique=False, nullable=False) 
    classes = db.relationship('Classes',backref=db.backref('enrollment',lazy=True, ))
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'),unique=False, nullable=False)
    student = db.relationship('Students',backref=db.backref('enrollment',lazy=True, ))
    
    grade = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self): 
        return '<Enrollment %r>' % self.class_id

class Classes(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    courseName = db.Column(db.String, unique=True, nullable=False) 
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'),unique=False, nullable=False)
    teacher = db.relationship('Teachers',backref=db.backref('class',lazy=True, ))

    numberEnrolled = db.Column(db.Integer, unique=False, nullable=False) 
    capacity = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.String, unique=False, nullable=False) 

class Teachers(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=False, nullable=False) 

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True, nullable=False)
    user = db.relationship('Users',backref=db.backref('teacher',lazy=True ))


@app.route('/')
def index():
    print('landing')
    if(not current_user.is_authenticated):
        print('not_auth')
        return redirect(url_for('login'))
    print('authenticated')
    return render_template('studentView.html')


@login_manager.user_loader
def load_user(id):
    return Users.query.get(id)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/login', methods =['GET','POST'], endpoint='login')
def Login():
    print('postLogin')
    if request.method == 'GET':
        if(current_user.is_authenticated):
            return redirect(url_for('studentView.html'))
        return render_template('login.html')

    if request.method == 'POST':
        print(request.form['username'])
        user = Users.query.filter_by(username = request.form['username'])

        if user is None:
            return redirect(url_for('login'))
        
        user = user.first()
        
        if user is None:
            return redirect(url_for('login'))

        if not user.checkPassword(request.form['password']):
            return redirect(url_for('login'))

        login_user(user)
        print (user.userLevel)
        return render_template('studentView.html')

@app.route('/index')
def deez():
    print('bofa')
    return 'bofa'

@app.route('/studentView/<userid>', methods = ['GET'],endpoint = 'studentView')
def showStudentClasses(userid):
    classes = db.session.query(Classes.courseName, Teachers.name, Classes.time,Classes.numberEnrolled).filter(Enrollment.class_id == Classes.id,Classes.teacher_id == Teachers.id,Enrollment.student_id == Students.id,Students.user_id == Users.id,Users.id == userid).all()
    print(classes)
    
    data = []
    for row in classes:
        data.append(list(row))

    return jsonify(data)
    

@app.route('/studentView/offeredCourses/<userid>', methods = ['GET'],endpoint = 'studentView/courses')
def showStudentClasses(userid):
    classes = db.session.query(Classes.courseName, Teachers.name, Classes.time,Classes.numberEnrolled).filter(Enrollment.class_id == Classes.id,Classes.teacher_id == Teachers.id,Enrollment.student_id == Students.id,Students.user_id == Users.id,Users.id != userid).all()
    print(classes)
    
    data = []
    for row in classes:
        data.append(list(row))

    return 0

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
