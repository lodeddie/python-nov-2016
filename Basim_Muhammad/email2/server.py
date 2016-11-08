from flask import Flask,render_template,request,redirect,flash,session

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

mysql = MySQLConnector(app, 'emails')
@app.route('/')
def index():
	# all_query = mysql.query_db("SELECT * FROM emails")
	# print all_query
	return render_template('index.html')

@app.route('/results',methods=['POST'])
def results():
	if len(request.form['email']) < 1:
		flash("Email cannot be blank!")
		return redirect ('/')
	elif not EMAIL_REGEX.match(request.form['email']):
		flash("Invalid Email Address!")
		return redirect ('/')
	else:
		flash("Success!")
		insert_query = "INSERT INTO emails (email, created_at) VALUES (:email,NOW())"
		entry={'email':request.form['email']}
		mysql.query_db(insert_query,entry)
		return redirect('/show')
@app.route('/show')
def show_results():

	all_query = mysql.query_db("SELECT * FROM emails")
	print all_query
	return render_template('results.html',info=all_query)

app.run(debug=True)