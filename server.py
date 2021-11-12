from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///university.sqlite"
db = SQLAlchemy(app)


@app.route('/', endpoint='login')
def index():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
