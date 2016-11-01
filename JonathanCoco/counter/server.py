from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():

    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1

    return render_template("index.html")

@app.route('/reset', methods=['POST'])
def reset_counter():

    session['counter'] =0

    return redirect('/')

@app.route('/Plus2', methods=['POST'])
def incr_by_2():
    try:
        session['counter'] += 2
    except KeyError:
        session['counter'] = 1

    return render_template("index.html")


app.run(debug=True)
