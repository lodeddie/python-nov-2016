from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):

    if ('count' in request.session) == False:
        request.session['count'] = 1
        request.session['word'] = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

    print " we are  in index" + request.session['word']

    return render(request, 'randomwordapp/index.html')


def generate_random_word(request):
    print (request.method)
    if request.method == "POST":

        value = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])

        request.session['count'] = request.session['count'] + 1
        request.session['word']  = value

        return redirect('/')
    else:
        return redirect('/')
