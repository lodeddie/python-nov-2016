from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'property_search')

@app.route('/')
def index():

    return render_template('login.html')

@app.route('/Login', methods=['POST'])
def Login():
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.

    email = request.form['email']
    password = request.form['password']
    bError = False
    pw_hash = ''

    if len(email) < 1:
        flash("Email cannot be blank!")
        bError = True
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        bError = True

    if (bError == False):
        query = "SELECT * FROM users WHERE email = :email"
        # Then define a dictionary with key that matches :variable_name in query.
        data = {'email': email}
        # Run query with inserted data.
        users = mysql.query_db(query, data)
        # Friends should be a list with a single object,
        # so we pass the value at [0] to our template under alias one_friend.

        if (len(users) == 0):
            flash("Email Address does  not exist")
            bError = True

        if bError == False:
            user = users[0];

            if (bcrypt.check_password_hash(user['pw_hash'], password)) == False:
                bError = True
                flash("Passwords do not match")

        if bError == True:
            return render_template('login.html')
        else:
            session['user'] = users[0];

            users = mysql.query_db("SELECT * FROM users")
            return render_template('user_listing.html', all_users=users)

    else:
        return render_template('login.html')



@app.route('/LaunchRegistration', methods=['POST'])
def LaunchRegistration():

    return render_template('Registration.html', name='', email='', phone='')


@app.route('/Register', methods=['POST'])
def Register():

    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    name =  request.form['name']
    phone = request.form['phone']
    bError = False
    pw_hash = ''

    if len(email) < 1:
        flash("Email cannot be blank!")
        bError = True
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        bError = True

    if (password <> confirm_password ):
        flash("Passwords do not match")
        bError = True

    if len(password) < 8:
        flash("Invalid password, must be at least 8 characters")
        bErrror = True
    else:
        pw_hash = bcrypt.generate_password_hash(password)

    if (bError == False):

        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "INSERT INTO users (email, pw_hash, name, phone,  created_dt) VALUES (:email, :pw_hash, :name, :phone, NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'email': email,
                 'pw_hash': pw_hash,
                 'name': name,
                 'phone': phone
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)


        #user is registered, launch the listing page

        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': email}
        users = mysql.query_db(query, data)
        session['user'] = users[0];
        users = mysql.query_db("SELECT * FROM users")
        return render_template('user_listing.html', all_users=users)
    else:
        return render_template('Registration.html', name=name, email=email, phone=phone)

@app.route('/user/<id>/delete', methods=['POST'])
def destroy(id):

    query = "DELETE FROM users WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)

    users = mysql.query_db("SELECT * FROM users")
    return render_template('user_listing.html', all_users=users)


@app.route('/user/<id>/edit', methods=['POST'])
def edit(id):

    query = "SELECT * FROM users WHERE id = :id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'id': id}
    # Run query with inserted data.
    users = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.

    return render_template('user_edit_admin.html', user=users[0])


@app.route('/user/<id>/update', methods=['POST'])
def update(id):

    email = request.form['email']
    name =  request.form['name']
    phone = request.form['phone']

    query = "UPDATE users SET email='{}', name='{}', phone='{}' where id={}".format(email, name, phone, id)

    print query
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': email,
             'name': name,
             'phone': phone,
             'id': id
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query)

    query = "SELECT * FROM users"

    # Run query with inserted data.
    users = mysql.query_db(query)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.

    return render_template('user_listing.html', all_users=users)


app.run(debug=True)
