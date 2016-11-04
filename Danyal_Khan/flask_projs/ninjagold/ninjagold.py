from flask import Flask, render_template, request, redirect, session
import random
import time
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'



@app.route('/')
def mainpage():
	if "gold" in session:
		pass
	else: 
		session['gold']=int(0)
	return render_template("index.html")


@app.route('/process', methods=['POST'])
def makemoney():
	if request.form['action']=='farm':
		# currentTime= time.strftime.("%r") for the time stamp on
		session['add']=random.randint(10,20)
		session['gold']+=session['add']
		if 'result' in session:
			session['result']= "Earned " + str((session['add']))+" golds from the farm" +str("\n")+ str(session['result'])
		else:
			session ['result']= ""

	elif request.form['action'] == 'cave':
		session['add']=random.randint(5,10)
		session['gold']+=session['add']
		if 'result' in session:
			session['result']= str("\n")+"Earned " + str((session['add']))+" golds from the cave" +str("\n")+ str(session['result'])
		else:
			session ['result']= ""

	elif request.form['action'] == 'house':
		session['add']=random.randint(2,5)
		session['gold']+=session['add']
		if 'result' in session:
			session['result']= "Earned " + str((session['add']))+" golds from the house" +str("\n")+ str(session['result'])
		else:
			session ['result']= ""
	elif request.form['action'] == 'casino':
		session['add']=random.randint(-50,50)
		session['gold']+=session['add']
		if 'result' in session:
			session['result']= "Earned " + str((session['add']))+" golds from the casino" +str("\n")+ str(session['result'])
		else:
			session ['result']= ""
	

	return redirect('/')




# @app.route('/farm')
# def robfarm():
# 	session['gold']+=random.randint(10,20)	
# 	return render_template("index.html")

# @app.route('/cave')
# def robcave():
# 	session['gold']+=random.randint(5,10)	
# 	return render_template("index.html")

# @app.route('/house')
# def robhouse():
# 	session['gold']+=random.randint(2,5)	
# 	return render_template("index.html")

# @app.route('/casino')
# def gamble():
# 	session['gold']+=random.randint(-50,50)	
# 	return render_template("index.html")


app.run(debug=True)

