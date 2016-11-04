from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
	if "counter" in session:
		session['counter']+=1
	else: 
		session['counter']=1

	return render_template("index.html", counter=session['counter'])

@app.route('/two')
def double():
	if "counter" in session:
		session['counter']+=1
	else: 
		session['counter']=1
	return redirect("/")

@app.route('/hack')
def clear():
	if "counter" in session:
		session['counter']=0
	else: 
		session['counter']=0
	return redirect("/")

app.run(debug=True)