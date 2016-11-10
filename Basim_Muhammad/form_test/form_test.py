from flask import Flask,render_template,request,redirect,session  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/users',methods=['POST']) 
def create_user():
	print 'Got post info'
	session['name']=request.form['name']
	session['email']=request.form['email']
	return redirect('/show')

@app.route('/show')
def show_user():
  return render_template('user.html', name=session['name'], email=session['email'])

app.run(debug=True) 