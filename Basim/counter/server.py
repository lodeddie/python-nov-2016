from flask import Flask,render_template,request,redirect,session  # Import Flask to allow us to create our app.
app = Flask(__name__)   
app.secret_key = 'ThisIsSecret' 

@app.route('/')
def hello_world():
	if 'counter' in session:
		session['counter']+=1
	else:
		session['counter']=1
	return render_template('index.html',counter=session['counter'])

app.run(debug=True) 