from flask import Flask, render_template, request, redirect, session
import random
import time

app = Flask(__name__)
app.secret_key = "ThisIsSecret"

@app.route('/')
def index():

    session['your_gold'] = 0
    session['your_activities'] = []

    return render_template("index.html")


@app.route('/process_money', methods=['POST'])
def process_money():

    CurrMoney = int(session['your_gold'])
    house = request.form['building']
    color = 'green'
    activity_item = {}

    money = 0
    activity = ''

    if house == "farm":
        money = random.randrange(10, 20)
    elif house == "cave":
        money = random.randrange(5, 10)
    elif house == "house":
        money = random.randrange(2, 5)
    elif house == "casino":
        money =  random.randrange(-50, 50)

    if money > 0:
        activity = 'Earned {} from the {} on ({}).'.format(money, house, time.strftime("%c"))
    else:
        activity = 'Lost {} from the {} on ({}). Ouch!!!'.format(money, house, time.strftime("%c"))

    CurrMoney = CurrMoney + money

    if money < 0:
        color = 'red'

    activity_item['activity'] = activity
    activity_item['color']    = color

    session['your_gold'] = CurrMoney
    session['your_activities'].insert(0, activity_item)

    for activity in session['your_activities']:
        print activity['activity'], activity['color']



    return render_template("index.html")


@app.route('/reset', methods=['POST'])
def reset():

    return redirect('/')


app.run(debug=True)
