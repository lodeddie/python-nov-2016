from __future__ import unicode_literals
import bcrypt
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    """docstring for UserManager"""
    def register(self, account):
          errors=[]
          if len(account['first_name']) < 1:
            errors.append('Please enter a First Name')
          if len(account['last_name']) < 1:
            errors.append('Please enter a Last Name')

          if len(account['email']) < 3:
            errors.append('Email is not long enough')
            
            
          elif not EMAIL_REGEX.match(account['email']):
            errors.append('Not a valid Email')
            
          
          if len(account['password']) < 1:
            errors.append('Please enter a password')
          if len(account['verify_password']) < 1:
            errors.append('Please verify password')   
          
          if not account['password']== account['verify_password']:
            errors.append('Passwords dont match')
        
          return errors
        

    def login(self, email, password):
        attempt = User.objects.filter(email=email)
        errors=[]

        
        if len(attempt)<1:
            errors.append('No Email found')
            return errors

        testpassword= password.encode()
        hashdb=attempt[0].pwhashed.encode()
        testhashed= bcrypt.hashpw(testpassword, hashdb)
        
        if testhashed != hashdb:
            errors.append('Password doesnt match')

        return errors
        # print '*'*50
        # print account
        # print '*'*50
        # print account['email']
        # print '*'*50
        
        
        

class User(models.Model):
      first_name = models.TextField(max_length=50)
      last_name = models.TextField(max_length=50)
      email = models.EmailField(max_length=100)
      pwhashed = models.TextField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # *************************
      # Connect an instance of UserManager to our User model overwriting 
      # the old hidden objects key with a new one with extra properties!!!
      objects = UserManager()
