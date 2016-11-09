
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)
import re

mysql = MySQLConnector(app,'loginsdb')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'KeepItSecretKeepItSafe'


@app.route('/')
def index():
    return render_template('index.html')



# @app.route('/check', methods=['POST'])
@app.route('/register', methods=['POST'])
def checking():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
    elif len(request.form['first_name']) < 2:
        flash("First Name must be longer and only contain letters!")
        return redirect('/')
    elif len(request.form['last_name']) < 2:
        flash("Last Name must be longer and only contain letters!")
        return redirect('/')
    elif len(request.form['password']) < 8:
        flash("Password must be longer than 8 characters!")
        return redirect('/')
    elif not request.form['password']==request.form['password_conf']:
        flash("Passwords dont match!")
        return redirect('/')
 
 
    else:
        flash("Success!")
        password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(password)
        query = "INSERT INTO creds (email, first_name, last_name, password, created_at, updated_at) VALUES (:email, :first_name, :last_name, :password, NOW(), NOW())"
        data = {
             'email': request.form['email'],
             'first_name': request.form['first_name'], 
             'last_name': request.form['last_name'],
             'password': pw_hash
           }
        mysql.query_db(query, data)
        database= mysql.query_db("SELECT * FROM creds")
        print database
        return render_template('success.html', account=database)

@app.route('/login', methods=['POST'])
def login():
     email = request.form['email']
     password = request.form['password']
     user_query = "SELECT * FROM creds WHERE email = :email LIMIT 1"
     query_data = { 'email': email }
     user = mysql.query_db(user_query, query_data) # user will be returned in a list
     if bcrypt.check_password_hash(user[0]['password'], password):
        return render_template('login.html')
     else:
        flash("Email or password does not match")
        return redirect('/')

 


app.run(debug=True)