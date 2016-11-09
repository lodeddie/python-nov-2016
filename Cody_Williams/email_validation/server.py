from flask import Flask, render_template, redirect, session, flash, request
from mysqlconnection import MySQLConnector
import re

app = Flask(__name__)

mysql = MySQLConnector(app, 'flaskEmail')

app.secret_key = "shh don't tell"

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/emails', methods=['POST'])
def create():
	#check for valid email
	email = request.form['email']
	if not email_regex.match(email):
		flash('you must provide a valid email address.')
		return redirect('/')
	else if len(email) < 1:
		flash('email cannot be blank')
	else:
		#put in the database
		query = "INSERT INTO users (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
		data = {
			"email" : email,
		}
		mysql.query_db(query, data)
		return redirect('/results')

@app.route('/results')
def show():
	query = "SELECT email FROM users"
	emails = mysql.query_db(query)
	lastEmail = emails[len(emails) - 1]

	return render_template('results.html', emails=emails, lastEmail=lastEmail)

app.run(debug=True)