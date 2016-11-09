import re
from flask import Flask, render_template, request, redirect, flash
from mysqlconnection import MySQLConnector

app = Flask (__name__)
mysql = MySQLConnector(app, "email_python_test")
app.secret_key = "email"

@app.route("/")
def index():
	query = "SELECT * FROM users"
	emails = mysql.query_db(query)
	return render_template("index.html", all_emails=emails)

@app.route("/validate", methods=["POST"])
def validate():
	has_error = False
	response =""
	email = request.form["email"]
	if len(email) == 0:
		has_error = True
		response += "Email is not valid.... Enter an Email"
	if len(email) !=0:
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		if not EMAIL_REGEX.match(email):
			print "*"*200
			print "Works"
			has_error = True
			response += "Email not valid... written incorrectly"
	if has_error == True:
		flash(response)
		return redirect('/')
	else:
		query="INSERT INTO users(email, created_at) VALUES (:email, NOW())"
		data={
			"email": email
			}
		flash("The email address you entered ---- is a VALID email address! Thank you!")
		mysql.query_db(query,data)
		return redirect('/success')
@app.route("/success")
def success():
	query = "SELECT * FROM users"
	emails = mysql.query_db(query)
	return render_template("success.html", all_emails=emails)
@app.route("/delete/<email_id>")
def delete(email_id):
	query = "DELETE FROM users WHERE id = :delete_id"
	data={
		'delete_id': email_id
		}
	mysql.query_db(query,data)
	return redirect("/success")

app.run(debug=True)
