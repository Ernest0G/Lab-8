from enum import unique
from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.sqlite"
db = SQLAlchemy(app)

class Users(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String, unique=True, nullable=False) 
    password = db.Column(db.String, unique=False, nullable=False)

    def __repr__(self): 
        return '<Users %r>' % self.title

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
    

@app.route('/', endpoint='login')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
