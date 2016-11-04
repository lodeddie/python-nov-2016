from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
app = Flask(__name__)
mysql = MySQLConnector(app,'email')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def index():
    query = "SELECT * FROM email"                           
    email = mysql.query_db(query)

    return render_template('index.html', all_email='email')

@app.route('/check', methods=['POST'])
def checking():
    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        return redirect('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        return redirect('/')
 
    else:
        flash("Success!")
        
        query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
        data = {'email': request.form['email']}
        mysql.query_db(query, data)
        database= mysql.query_db("SELECT * FROM email")
        print database
        return render_template('success.html', all_emails=database)

 


app.run(debug=True)