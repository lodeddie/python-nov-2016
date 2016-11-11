from django.shortcuts import render, redirect
from django.conf.urls import url

# Create your views here.
def index(request):
	return render(request, 'index.html')

def process(request):
	
	if "counter" in request.session:
			request.session['counter']+=1
	else: 
			request.session['counter']=1
	
	request.session['data']=request.POST
	
	return redirect('/results')

def results(request):

	return render(request, 'results.html')







# def process(request):
# 	print "*" *100
# 	print request.POST
# 	print "*" *100
# 	return render(request, 'results.html')