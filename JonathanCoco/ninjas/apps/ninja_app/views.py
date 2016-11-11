from django.shortcuts import render, redirect, HttpResponse
import random
import string

# Create your views here.
def index(request):

    return render(request, 'ninja_app/index.html')


# Create your views here.
def ninja(request, ninja):

    if (ninja == ""):
        context = {'color':'ALL'}
    elif (ninja == "red"):
        context = {'color':'red'}
    elif (ninja == "blue"):
        context = {'color':'blue'}
    elif (ninja == "orange"):
        context = {'color':'orange'}
    elif (ninja == "purple"):
        context = {'color':'purple'}
    else:
        context = {'color':'none'}

    print context

    return render(request, 'ninja_app/ninja.html', context)
