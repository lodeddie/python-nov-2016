from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret"
mysql = MySQLConnector(app,'email_validation')


@app.route('/')
def index():
    #friends = mysql.query_db("SELECT * FROM friends")
    #return render_template('index.html', all_friends=friends)

    return render_template('index.html')

@app.route('/email', methods=['POST'])
def create():

    bError = False;

    if len(request.form['email']) < 1:
        flash("Email cannot be blank!")
        bError = True;
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")
        bError = True;

    if bError:
            return redirect('/')
    else:
        # Write query as a string. Notice how we have multiple values
        # we want to insert into our query.
        query = "INSERT INTO emails_entered (email, created_dt) VALUES (:email, NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'email': request.form['email']
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)

        # Write query to select specific user by id. At every point where
        # we want to insert data, we write ":" and variable name.
        query = "SELECT * FROM emails_entered order by created_dt"
        # Run query with inserted data.
        emails = mysql.query_db(query)
        # Friends should be a list with a single object,
        # so we pass the value at [0] to our template under alias one_friend.

        return render_template('success.html', all_emails=emails, email=request.form['email'])

@app.route('/delete', methods=['POST'])
def delete():

    id = request.form.get('resultlist')

    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "DELETE FROM emails_entered WHERE ID = {}".format(id)

    # We'll then create a dictionary of data from the POST data received.

    print query

    # Run query, with dictionary values injected into the query.
    mysql.query_db(query)

    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM emails_entered order by created_dt"
    # Run query with inserted data.
    emails = mysql.query_db(query)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.

    return render_template('success.html', all_emails=emails,email='')

app.run(debug=True)
