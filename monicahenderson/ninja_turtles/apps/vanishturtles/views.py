from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'vanishturtles/index.html' )

def turtle_images(request, color):
    if color == '':
        return render(request, 'vanishturtles/allturtles.html')
    if color == 'blue':
        return render(request, 'vanishturtles/leonardo.html')
    elif color == 'orange':
        return render(request, 'vanishturtles/michelangelo.html')
    elif color == 'red':
        return render(request, 'vanishturtles/raphael.html')
    elif color == 'purple':
        return render(request, 'vanishturtles/donatello.html')
    else:
        return render(request, 'vanishturtles/nohack.html')
