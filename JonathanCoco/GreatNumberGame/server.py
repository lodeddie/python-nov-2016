from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():

    session['number'] = random.randrange(0, 100)

    return render_template("index.html", state="init", value=session['number'])

@app.route('/play_again', methods=['POST'])
def reset_counter():

    session.pop('number')
    return redirect('/')

@app.route('/submit_guess', methods=['POST'])
def submit_guess():

    print session['number']

    if (int(session['number']) == int(request.form['user_guess'])):
        return render_template("index.html", state="found")

    elif (int(session['number']) < int(request.form['user_guess'])):
        return render_template("index.html", state="high" )
    else:
        return render_template("index.html", state="low")


app.run(debug=True)
