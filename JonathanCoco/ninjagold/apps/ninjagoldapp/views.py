from django.shortcuts import render, redirect, HttpResponse
import random
import time

# Create your views here.
def index(request):

    if ('your_gold' in request.session) == False:
        request.session['your_gold'] = 0
        request.session['your_activities'] = []

    return render(request, 'ninjagoldapp/index.html')

def process_money(request, building):

    CurrMoney = int(request.session['your_gold'])

    house = building
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

    request.session['your_gold'] = CurrMoney
    request.session['your_activities'].insert(0, activity_item)

    for activity in request.session['your_activities']:
        print activity['activity'], activity['color']

    return render(request, 'ninjagoldapp/index.html')


def reset(request):

    try:
        del request.session['your_gold']
        del request.session['your_activities']
    except Exception as e:
        pass

    return redirect('/')
