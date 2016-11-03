from flask import Flask, render_template, request, redirect, session, flash

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
BIRTHDATE_REGEX = re.compile(r'^[\d\d]+/[\d\d]+/[\d\d\d\d]')
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/', methods=['GET'])
def index():

    return render_template("index.html")


@app.route('/process', methods=['POST'])
def process():
    print "what up"

    if len(request.form['first_name']) < 1:
        flash("First Name cannot be blank!")
    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be blank!")
    if len(request.form['password']) < 1:
        flash("Password cannot be blank!")

    if (request.form['password'] != request.form['confirm_password']):
        flash("Passwor/Confirm Passord does not match")

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")

    if not BIRTHDATE_REGEX.match(request.form['birth_date']):
        flash("Invalid Birth Date!")


    return redirect('/')




app.run(debug=True)
