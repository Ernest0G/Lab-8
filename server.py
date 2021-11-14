from enum import unique
from flask import Flask, jsonify, request, render_template, redirect, url_for, session
from flask_login.utils import login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship
from flask_login import current_user, login_user, LoginManager
from flask_admin import Admin

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.sqlite"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.secret_key = 'secret-key'

class Users(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String, unique=True, nullable=False) 
    password = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self): 
        return '<Users %r>' % self.title

    def checkPassword(self,password):
        return self.password == password
'''
class Students(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=False, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'),unique=True,nullable=False)
    
    user = db.relationship('Users',backref=db.backref('students',lazy=True))

    def __repr__(self): 
        return '<Students %r>' % self.title

class Enrollment(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    class_id = db.Column(db.Integer, db.ForeignKey('Classes.id'),unique=True, nullable=False) 
    student_id = db.Column(db.Integer, db.ForeignKey('Students.id'),unique=True, nullable=False)
    grade = db.Column(db.Integer, unique=False, nullable=True)

class Classes(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    courseName = db.Column(db.String, unique=True, nullable=False) 
    teacher_id = db.Column(db.Integer, db.ForeignKey('Teachers.id'),unique=True, nullable=False) 
    numberEnrolled = db.Column(db.Integer, unique=False, nullable=False) 
    capacity = db.Column(db.Integer, unique=False, nullable=False)
    time = db.Column(db.String, unique=False, nullable=False) 

class Teachers(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String, unique=False, nullable=False) 
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'),unique=True, nullable=False)
    
'''


@app.route('/', endpoint='landing')
def index():
    return render_template('login.html')

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

@login_manager.user_loader
def load_user(id):
    return Users.get(id)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
