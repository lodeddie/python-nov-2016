from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt
from django.core.urlresolvers import reverse

def index(request):
	return render(request, 'login_registration_app/index.html')

def create_account(request):
	# print '* request.post'*10
	# print request.POST
	result= User.objects.register(account=request.POST)
	
	if len(result)>0:
		for message in result:
			messages.warning(request, message)
			print message
		return redirect(reverse('logreg:index'))
	else:
			first_name = request.POST['first_name']
			last_name = request.POST['last_name']
			email = request.POST['email']

			password = request.POST['password'].encode()
			pwhashed = bcrypt.hashpw(password, bcrypt.gensalt())

			User.objects.create(first_name=first_name, last_name=last_name, email=email, pwhashed=pwhashed)
			
			context={'data':User.objects.filter(email=request.POST['email'])}
			

			return render(request, 'login_registration_app/success.html', context)



def login(request):
	valid = User.objects.login(email=request.POST['email'], password=request.POST['password'])
	if len(valid)>0:
		for message in valid:
			messages.warning(request, message)
		return redirect(reverse('logreg:index'))
	
	else:
	
		context={'data':User.objects.filter(email=request.POST['email'])}
		return render(request, 'login_registration_app/success.html', context)






