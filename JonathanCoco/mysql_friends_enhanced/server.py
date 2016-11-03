from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    friends = mysql.query_db("SELECT * FROM friends")
    return render_template('index.html', all_friends=friends)

@app.route('/friends', methods=['POST'])
def create():

    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)

    return redirect('/')

@app.route('/friends/<id>/edit', methods=['POST'])
def edit(id):
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.

    query = "SELECT * FROM friends WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.

    #return render_template('edit_friend.html', all_friends=friends)
    return render_template('edit_friend.html', friend=friends[0])

@app.route('/friends/<id>/update', methods=['POST'])
def update(id):


    query = "UPDATE friends  SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': id
           }

    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/delete', methods=['POST'])
def destroy(id):

    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)
