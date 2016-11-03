# I made some minor changes since the video:
	# - Instead of using a global array (aka list) as our dataStore I used session
	# - I cleaned up the string, as it wasn't formatted properly


#import dependencies
from flask import Flask, render_template, session, request, redirect
from random import randint
import time

#initialize our flask app
app = Flask(__name__)

#secret key for sessions
app.secret_key = "whatever"

#our first route will be the root route, or '/' (aka localhost:5000)
@app.route('/')
def hello_world():
	# session['gold'] is our gold counter, we're checking to see if 'gold'
	# is in session and if not we're adding it to session and setting it to 0
	if not('gold' in session):
		session['gold'] = 0
	#session['activities'] will be an array (aka list) of objects (aka dictionaries)
	# where each object (aka dictionary) is the activity
	if not('activities' in session):
		session['activities'] = []
	return render_template('index.html')

#this route will handle our form, it matches the 'action' attribute of our form and knows
#this will be a POST request because the second argument, or 'methods=["POST"]'
@app.route('/process_money', methods=["POST"])
def create():
	#we use a series of if checks to decide how much gold we are giving the user
	#this is based on the hidden 'location' attribute of each of our four forms
	#gold amount is the only part that is unique to each location so that is all we
	#need to do in our if checks
	if(request.form['location'] == 'farm'):
		gold = randint(10,20)
	if (request.form['location'] == 'cave'):
		gold = randint(5, 10)
	if (request.form['location'] == 'house'):
		gold = randint(2, 5)
	if (request.form['location'] == 'casino'):
		gold = randint(-50, 50)

	#here we increase the amount of gold stored in session
	session['gold'] += gold
	#we're using the time module to grab the current time and strftime to format it
	currentTime = time.strftime("%G/%m/%d %r")
	#we're grabbing the value of the hidden input 'location' from the form data that was submitted
	#and saving it into a variable called location
	location = request.form['location']
	#now we build a string by concatenating the variables where necessary
	string = 'Earned ' + str(gold) + ' golds from the ' + location + '! (' + currentTime + ')'

	#lets create an activity object (aka dictionary) to push into session['activities']
	activity = {}

	#we're checking to see if the gold amount was positive or negative
	#if positive we save the string 'green' into the color attribute of the activity object (aka dictionary)
	#if negative we save the string 'red' into the color attribute of the activity object (aka dictionary)
	#the color attribute will define the class of our html element on the front-end  
	if gold > 0:
		activity['color'] = 'green'
	else:
		activity['color'] = 'red'

	#after setting the color attribute we save the string we built into the
	#msg attribute of the activity object (aka dictionary)
	activity['msg'] = string
	#now we insert that activity object (aka dictionary)
	#at the 0th element of our session['activities'] array (aka list)
	session['activities'].insert(0, activity)
	#finally we redirect to the homepage, or the root route
	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	#here we reset the session['gold'] amount to 0
	session['gold'] = 0
	#and reset the session['activities'] array (aka list) back to an empty array (aka list)
	session['activities'] = []
	#and again, redirect to the homepage, or root route
	return redirect('/')

app.run(debug=True)
