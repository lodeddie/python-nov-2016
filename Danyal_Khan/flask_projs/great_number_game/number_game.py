from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if 'number' in session:
		pass 
	else:
		session['number']= random.randint(0,100)
	print session['number']
	return render_template("index.html")

@app.route('/answer', methods=['POST'])
def attempt():
	guess=request.form['guess']
	if session['number']>int(guess):
		session['display']="Too Low"
	elif session['number']<int(guess):
		session['display']="Too High"
	elif session['number']==int(guess):
		session['display']="Correct!!!!"
	else:
		session['display']="You broke it!"

	return redirect('/')

app.run(debug=True)