from enum import unique
from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
from flask_login import current_user, login_user, LoginManager, UserMixin
from flask_admin import Admin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.sqlite"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'secret-key'

class Users(UserMixin,db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String, unique=True, nullable=False) 
    password = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self): 
        return '<Users %r>' % self.username

    def checkPassword(self,password):
        return self.password == password

class Students(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=False, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True,nullable=False)
    
    user = db.relationship('users',backref=db.backref('students',lazy=True ))

    def __repr__(self): 
        return '<Students %r>' % self.name

class Enrollment(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'),unique=True, nullable=False) 
    classes = db.relationship('class',backref=db.backref('enrollment',lazy=True, ))
    
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'),unique=False, nullable=False)
    student = db.relationship('students',backref=db.backref('enrollment',lazy=True, ))
    
    grade = db.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self): 
        return '<Enrollment %r>' % self.class_id

class Classes(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    courseName = db.Column(db.String, unique=True, nullable=False) 
    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.id'),unique=False, nullable=False)
    teacher = db.relationship('teachers',backref=db.backref('Classes',lazy=True, ))

    numberEnrolled = db.Column(db.Integer, unique=False, nullable=False) 
    capacity = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.String, unique=False, nullable=False) 

class Teachers(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=False, nullable=False) 

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True, nullable=False)
    user = db.relationship('users',backref=db.backref('teachers',lazy=True ))



@app.route('/', endpoint='landing')
def index():
    return render_template('studentView.html')

@login_manager.user_loader
def load_user(id):
    return Users.get(id)

@app.route('/login', methods =['POST'], endpoint='login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('/index'))
    user = Users.query.filter_by(username = request.json['username']).first()
    if user is None or not user.check_password(request.json['password']):
        return redirect(url_for('login'))
    login_user(user)
    return redirect(url_for('index'))


@app.route('/index', endpoint='index')
@login_required
def index():
    return render_template('index.html')

@app.route('/studentView/<studentid>', methods = ['GET'],endpoint = 'studentView')
def showStudentClasses(studentid):
    classes = Enrollment.query.filter_by(id = studentid)
    print(classes)
    return classes


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
