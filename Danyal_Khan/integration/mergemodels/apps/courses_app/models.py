from __future__ import unicode_literals

from django.db import models

from ..login_registration_app.models import User

class CourseManager(models.Manager):
    def add_user_to_course(self, form_data):
        # First find the course
        course = self.get(id=form_data['course'])
        # Then grab the user
        user = User.objects.get(id=form_data['user'])
        # Add the user to the course
        course.users.add(user)
        #And finally save the course
        course.save()

class Course(models.Model):
	"""docstring for blogs"""
	course_name = models.CharField(max_length=100)
	description = models.TextField(max_length=500)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	objects= CourseManager()
	users = models.ManyToManyField('login_registration_app.User', related_name='courses')
