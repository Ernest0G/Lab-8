from flask import Flask
from flask_login.login_manager import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import UserMixin, LoginManager, current_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)
login = LoginManager(app)

@login.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)

class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin = Admin(app)
admin.add_view(MyModelView(Users, db.session))

@app.route('/login')
def login():
    user = Users.query.get(1)
    login_user(user)
    return 'Logged in'

if __name__ == '__main__':
    app.run(debug=True) 