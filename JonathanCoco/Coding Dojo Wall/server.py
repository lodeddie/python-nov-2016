from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt

import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app = Flask(__name__)
app.secret_key = "ThisIsSecret"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'coding_dojo_wall')

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

            if (bcrypt.check_password_hash(user['password'], password)) == False:
                bError = True
                flash("Passwords do not match")

        if bError == True:
            return render_template('login.html')
        else:
            session['user'] = users[0];

            messages = mysql.query_db("SELECT * FROM coding_dojo_wall_vw order by message_id desc, comment_created_dt asc, comment_id asc")
            return render_template('message_listing.html', messages=messages, curr_message=0)

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
    first_name =  request.form['first_name']
    last_name = request.form['last_name']

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
        query = "INSERT INTO users (email, password, first_name, last_name, created_dt, updated_dt) VALUES (:email, :pw_hash, :first_name, :last_name, NOW(), NOW())"
        # We'll then create a dictionary of data from the POST data received.
        data = {
                 'email': email,
                 'pw_hash': pw_hash,
                 'first_name': first_name,
                 'last_name': last_name
               }
        # Run query, with dictionary values injected into the query.
        mysql.query_db(query, data)


        #user is registered, launch the listing page

        query = "SELECT * FROM users WHERE email = :email"
        data = {'email': email}
        users = mysql.query_db(query, data)
        session['user'] = users[0];
        messages = mysql.query_db("SELECT * FROM coding_dojo_wall_vw order by message_id desc, comment_created_dt asc, comment_id asc")
        return render_template('message_listing.html', messages=messages)
    else:
        return render_template('Registration.html', first_name=first_name, last_name=last_name, email=email)



@app.route('/message/post/<id>', methods=['POST'])
def post(id):

    message = request.form['message']
    user = session['user']

    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO messages (user_id,  message, created_dt, updated_dt) VALUES (:user_id, :message, NOW(), NOW())"

    # We'll then create a dictionary of data from the POST data received.
    data = {
             'user_id': user['id'],
             'message': message
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)


    messages = mysql.query_db("SELECT * FROM coding_dojo_wall_vw order by message_id desc, comment_created_dt asc, comment_id asc")
    return render_template('message_listing.html', messages=messages)


@app.route('/message/post_comment/<id>', methods=['POST'])
def post_comment(id):

    comment = request.form['comment']
    user = session['user']

    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO comments (message_id, user_id,  comment, created_dt, updated_dt) VALUES (:message_id, :user_id, :comment, NOW(), NOW())"

    # We'll then create a dictionary of data from the POST data received.
    data = {
             'message_id': id,
             'user_id': user['id'],
             'comment': comment
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)


    messages = mysql.query_db("SELECT * FROM coding_dojo_wall_vw order by message_id desc, comment_created_dt asc, comment_id asc")
    return render_template('message_listing.html', messages=messages)


@app.route('/message/delete_comment/<id>', methods=['POST'])
def delete_comment(id):


    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "delete from comments where id = :id"

    # We'll then create a dictionary of data from the POST data received.
    data = {
             'id': id
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)


    messages = mysql.query_db("SELECT * FROM coding_dojo_wall_vw order by message_id desc, comment_created_dt asc, comment_id asc")
    return render_template('message_listing.html', messages=messages)




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
    first_name =  request.form['first_name']
    last_name = request.form['last_name']

    query = "UPDATE users SET email='{}', first_name='{}', last_name='{}' where id={}".format(email, first_name, last_name, id)

    print query
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'email': email,
             'first_name': first_name,
             'last_name': last_name,
             'id': id
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query)

    query = "SELECT * FROM users"
    users = mysql.query_db(query)
    return render_template('user_listing.html', all_users=users)

@app.route('/user/<id>/delete', methods=['POST'])
def delete(id):

    try:
        query = "DELETE FROM users WHERE id = :id"
        data = {'id': id}
        mysql.query_db(query, data)
    except Exception as e:
        flash("Selected user has created messages/comments and cannot be deleted")

    users = mysql.query_db("SELECT * FROM users")
    return render_template('user_listing.html', all_users=users)


@app.route('/admin', methods=['GET'])
def admin():


    query = "SELECT * FROM users order by last_name, first_name"
    users = mysql.query_db(query)
    return render_template('user_listing.html', all_users=users)

@app.route('/logoff', methods=['GET'])
def logoff():

    session.pop('user')

    return redirect('/')

@app.route('/message_listing', methods=['GET'])
def message_listing():
    messages = mysql.query_db("SELECT * FROM coding_dojo_wall_vw order by message_id desc, comment_created_dt asc, comment_id asc")
    return render_template('message_listing.html', messages=messages)



app.run(debug=True)
