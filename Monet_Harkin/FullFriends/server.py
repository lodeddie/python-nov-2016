import re
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')
app.secret_key = "secretfriends"

@app.route('/')
def index():
	if "form" not in session:
		session["form"]={}
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
	first= request.form['first_name']
	last= request.form['last_name']
	email= request.form['email']
	session["form"]=request.form
	EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
	if len(email) == 0:
		flash("NOT ADDED : Email required")
	elif len(first) == 0 or len(last) == 0:
		flash("NOT ADDED : Full name required")
	elif not EMAIL_REGEX.match(email):
		flash("NOT ADDED : Invalid email")
	else:
		session.pop("form")
		session["form"]={}
		query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
		data={
			'first_name': first,
			'last_name': last,
			'email': email
			}
		mysql.query_db(query, data)
	# add a friend to the database!
	return redirect('/')
@app.route('/friends/<friend_id>')
def update(friend_id):
	query = "SELECT * FROM friends WHERE id = :specific_id"
	data = {'specific_id':friend_id}
	friends = mysql.query_db(query, data)
	return render_template('update.html', one_friend=friends[0])
@app.route('/friend/<friend_id>/edit', methods=['POST'])
def edit(friend_id):
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, email = :email, updated_at = NOW() WHERE id = :id"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'email': request.form['email'],
			'id': friend_id
		}
	mysql.query_db(query,data)
	return redirect('/')
@app.route('/remove_friend/check', methods=['POST'])
def check():
	idcheck = request.form['idcheck']
	query = "SELECT * FROM friends WHERE id = :id"
	data = {'id': idcheck}
	friend =  mysql.query_db(query,data)
	return render_template('delete_friend.html', check_delete=friend[0])
@app.route('/friend/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):
	query = "DELETE FROM friends where id = :id"
	data = {'id': friend_id}
	mysql.query_db(query,data)
	return redirect('/')


app.run(debug=True)
