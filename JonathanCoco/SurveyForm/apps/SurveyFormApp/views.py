from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):

    if ('count' in request.session) == False:
        request.session['count'] = 0
        request.session['name'] = ''
        request.session['language'] = ''
        request.session['location'] = ''
        request.session['comment'] = ''

    return render(request, 'SurveyFormApp/index.html')


def submit_form(request):
    print (request.method)
    if request.method == "POST":

        request.session['count'] = request.session['count'] + 1

        request.session['name'] = request.POST['name']
        request.session['language'] = request.POST['language']
        request.session['location'] = request.POST['location']
        request.session['comment'] = request.POST['comment']

        return redirect('/result')
    else:
        return redirect('/')

def result(request):
    return render(request, 'SurveyFormApp/result.html')

def reset(request):

    try:
        del request.session['count']
        del request.session['name']
        del request.session['language']
        del request.session['location']
        del request.session['comment']
    except Exception as e:
        pass

    return redirect('/')


# Create your views here.
