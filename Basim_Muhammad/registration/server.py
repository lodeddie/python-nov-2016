from flask import Flask,render_template,request,redirect,flash,session
from flask.ext.bcrypt import Bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX=re.compile(r'^[A-Za-z]')

from mysqlconnection import MySQLConnector
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'ThisIsSecret'

mysql = MySQLConnector(app, 'users')
@app.route('/')
def index():
	# all_query = mysql.query_db("SELECT * FROM users")
	# print all_query
	return render_template('index.html')

@app.route('/login', methods=['POST'])
def login_data():
	if request.form['action']=='registration':
		first=request.form['first_name']
		last=request.form['last_name']
		email=request.form['email']
		password=request.form['password']
		confirm=request.form['password_confirmation']
		if len(first)<2 or len(last)<2 or len(email)<1 or len(password)<8:
			flash('All fields must be filled.Password must be longer than 8 characters')
			return redirect('/')
		elif confirm!=password:
			flash('Your password confirmation does not match your password')
			return redirect('/')
		elif not NAME_REGEX.match(first):
			flash('Name can only contain letters.')
			return redirect('/')
		elif not NAME_REGEX.match(last):
			flash('Name can only contain letters. ')
			return redirect('/')
		elif not EMAIL_REGEX.match(email):
			flash('Your email is not valid.')
			return redirect('/')
		else:
			pw_hash=bcrypt.generate_password_hash(password)
			query = "INSERT INTO users (first_name, last_name, email, pw_hash) VALUES (:first_name, :last_name, :email, :pw_hash)"
			data ={'first_name':first, 'last_name':last,'email':email,'pw_hash':pw_hash}
			mysql.query_db(query,data)
		print 'true'
		return redirect('/')
	else:
		email = request.form['email']
		password = request.form['password']
		user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
		query_data = { 'email': email }
		user = mysql.query_db(user_query, query_data)
		if user==[]:
			flash('Invalid Email')
			return redirect('/')
		elif not bcrypt.check_password_hash((user[0]['pw_hash']), password):
			flash('Invalid Password')
			return redirect ('/')
		else:
			flash('Log In Successful')
			return redirect('/')
app.run(debug=True)