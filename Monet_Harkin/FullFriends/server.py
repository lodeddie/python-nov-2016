from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
	query = "SELECT * FROM friends"
	friends = mysql.query_db(query)
	return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first, :last_name, :occupation, NOW(), NOW())"
	data={
		'first': request.form['first_name'],
		'last_name': request.form['last_name'],
		'occupation': request.form['occupation']
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
	query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation, updated_at = NOW() WHERE id = :id"
	data = {
			'first_name': request.form['first_name'],
			'last_name': request.form['last_name'],
			'occupation': request.form['occupation'],
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
