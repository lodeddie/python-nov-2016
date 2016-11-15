from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

def index(request):

    
    return render(request, 'email_app/index.html')

def check(request):
    
    message = ""
    if User.objects.login(request.POST["email"])==False:
        messages.warning(request, 'Invalid email')
        # email = Email(email=request.POST["email"])
     #    email.save()

     #    email = Email.objects.all()
     #    message = "The email address you entered {} is a VALID email address! Thank You".format(request.POST["email"])

        return redirect('/')
    else:
        messages.success(request, 'Email Successfully Stored!')
        User.objects.create(email=request.POST['email'])
        context={'data':User.objects.all()}

        return render (request,'email_app/success.html', context)
        

    