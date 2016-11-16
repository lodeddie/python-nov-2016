from django.shortcuts import render, redirect
from .models import Course
from ..login_registration_app.models import User

from django.core.urlresolvers import reverse
from django.db.models import Count

def index(request):
	
	context = {
		"courses" : Course.objects.all()
	}
	
	return render(request, 'courses_app/index.html', context)


def add(request):
	# name= request.POST['name']
	# description= request.POST['description']

	Course.objects.create(course_name=request.POST['name'], description=request.POST['description'])
	return redirect(reverse('courses:my_index'))
	

def destroy(request, id):
	context={
		"course" : Course.objects.get(id=id)
	}
	print context['course']
	return render(request, 'courses_app/destroy.html', context)




def remove(request, id):
	Course.objects.get(id=id).delete()
	return redirect(reverse('courses:my_index'))


def admin(request):
	context = {
        'users' : User.objects.all(),
        'courses' : Course.objects.annotate(students=Count('users')),
    }
	return render(request, 'courses_app/courses.html', context)

def create(request):
	Course.objects.add_user_to_course(request.POST)
	return redirect(reverse('courses:admin'))



	