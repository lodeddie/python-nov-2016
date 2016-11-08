from flask import Flask,render_template,request,redirect,session
# import the Connector function
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'friendsdb')
@app.route('/')
def index():
	friends = mysql.query_db("SELECT * FROM friends")
	for i in friends:
		print i
	return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
	data = {
		 'first_name': request.form['first_name'], 
		 'last_name':  request.form['last_name'],
		 'occupation': request.form['occupation']
	   }
	mysql.query_db(query,data)

	return redirect('/')


@app.route('/friends/<friend_id>')
def unique_friend(friend_id):
	query='Select * from friends where id= :specific_id'
	user_id={'specific_id':friend_id}
	user_info=mysql.query_db(query,user_id)
	print user_info[0]
	return render_template('friend.html',user_info=user_info[0])

@app.route('/update/<friend_id>', methods=['POST'])
def update_friend(friend_id):
	query="UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
	data={'id': friend_id,'first_name':request.form['update_first'],'last_name':request.form['update_last'],'occupation':request.form['update_occupation']}
	mysql.query_db(query,data)
	return redirect ('/')

@app.route('/delete/<friend_id>')
def delete_friend(friend_id):
	query="DELETE FROM friends WHERE id = :id"
	user_id={'id':friend_id} 
	mysql.query_db(query,user_id)
	return redirect('/')

app.run(debug=True)