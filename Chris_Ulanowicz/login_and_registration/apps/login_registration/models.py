from __future__ import unicode_literals

from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')
PASSWORD_REGEX1 = re.compile(r'.*?\d')
PASSWORD_REGEX2 = re.compile(r'.*?[A-Z]')
PASSWORD_REGEX3 = re.compile(r'.*?[a-z]')
PASSWORD_REGEX4 = re.compile(r'.*?[\$\!\?\%\&]')
# .*?\d    checks for at least one digit
# .*?[A-Z] checks for at least one uppercase letter
# .*?[a-z] checks for at least one lowercase letter
# .*?[!?%&_] checks for at least one special character

class UserManager(models.Manager):
	def register(self, user):
		print user
		errors = []
		if len(user['first_name']) < 2:
			errors.append('First name must be at least 2 characters')
		elif not ALPHA_REGEX.match(user['first_name']):
			errors.append('First name can only contain letters')
		if len(user['last_name']) < 2:
			errors.append('Last name must be at least 2 characters')
		elif not ALPHA_REGEX.match(user['last_name']):
			errors.append('Last name can only contain letters')
		if len(user['username']) < 1:
			errors.append('Username cannot be blank')
		elif User.objects.filter(username = user['username']).exists():
			errors.append('Username is taken')
		if len(user['email']) < 1:
			errors.append('Email cannot be blank')
		elif not EMAIL_REGEX.match(user['email']):
			errors.append("Email not valid")
		if len(user['password']) < 1:
			errors.append('Password cannot be blank')
		elif len(user['password']) < 8:
			errors.append('Password must be at least 8 characters')
		elif not PASSWORD_REGEX1.match(user['password']):
			errors.append('Password must contain at least 1 number')
		elif not PASSWORD_REGEX2.match(user['password']):
			errors.append('Password must contain at least 1 Uppercase letter')
		elif not PASSWORD_REGEX3.match(user['password']):
			errors.append('Password must contain at least 1 lowercase letter')
		elif not PASSWORD_REGEX4.match(user['password']):
			errors.append('Password must contain at least 1 special character i.e. $!?%&')
		elif user['password'] != user['confirm_password']:
			errors.append('Passwords do not match')
		# if birthdate is not before today
		if len(errors) > 0:
			return (False, errors)
		else:
			newUser = {
				'first_name': user['first_name'],
				'last_name': user['last_name'],
				'username': user['username'],
				'email': user['email'],
				'password': bcrypt.hashpw(user['password'].encode(), bcrypt.gensalt()),
				'birthdate': user['birthdate']
			}
			user = User.objects.create(**newUser)
			user.save()
			return (True, "registered", user.username)

	def login(self, user):
		if len(user['email']) < 1 or len(user['password']) < 1:
			return (False, "Make sure email and password fields are filled in")
		try:
			logUser = User.objects.get(email=user['email'])
		except:
			return (False, "Invalid email or password")
		if logUser.password == bcrypt.hashpw(user['password'].encode(), logUser.password.encode()):
			return (True, "logged in", logUser.username)
		else:
			return (False, "Invalid email or password")

class User(models.Model):
	first_name = models.CharField(max_length=60)
	last_name = models.CharField(max_length=60)
	username = models.CharField(max_length=45)
	email = models.EmailField(max_length=254)
	password = models.CharField(max_length=254)
	birthdate = models.DateField(auto_now=False)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()