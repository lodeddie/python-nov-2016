from flask import Flask, request, redirect, render_template, session, flash, jsonify
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

mysql = MySQLConnector(app,'my_posts')

@app.route('/')
def index_home():
    query = "SELECT * FROM posts"
    posts = mysql.query_db(query)
    return render_template('index.html', posts=posts)


@app.route('/post/create', methods=['POST'])
def create():
    query = "INSERT INTO posts(description, created_at, updated_at) VALUES('{}', now(), now())".format(request.form['post_text'])
    mysql.query_db(query)

    return_query = "SELECT * FROM posts"
    post = mysql.query_db(return_query)
    return render_template('partials/posts.html', posts=post)



app.run(debug=True)
