from flask import Flask, request, redirect, render_template, session, flash, jsonify
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

mysql = MySQLConnector(app,'notes')

@app.route('/')
def index_home():
    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)

    return render_template('index.html', notes=notes)


@app.route('/notes/create', methods=['POST'])
def create():

    query = "INSERT INTO notes(title, description, created_at, updated_at) VALUES('{}', '{}', now(), now())".format(request.form['add_title'], request.form['add_description'])

    mysql.query_db(query)

    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)

    return render_template('partials/notes.html', notes=notes )

#    return_query = "SELECT * FROM notes"
#    post = mysql.query_db(return_query)
#    return render_template('partials/notes.html', notes=notes)

@app.route('/notes/delete', methods=['POST'])
def delete():

    query = "delete from notes where id = {}".format(request.form['note_id'])

    mysql.query_db(query)

    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)

    return render_template('partials/notes.html', notes=notes )



@app.route('/notes/update', methods=['POST'])
def update():

    query = "update notes set title = '{}', description = '{}' where id = {}".format(request.form['title'], request.form['description'], request.form['note_id'] )

    mysql.query_db(query)

    query = "SELECT * FROM notes"
    notes = mysql.query_db(query)

    return render_template('partials/notes.html', notes=notes )




app.run(debug=True)
