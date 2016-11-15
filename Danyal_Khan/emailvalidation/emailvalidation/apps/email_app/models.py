from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class UserManager(models.Manager):
      def login(self, email):
          errors=[]
          if len(email) < 1:
            errors.append('Not long enough')
            # messages.success('Email Blank')
            print errors
            return (False)
          elif not EMAIL_REGEX.match(email):
            errors.append('Not a valid Email')
            # messages.success( 'Not a valid Email')
            print errors
            return (False)
 
          else:
           # messages.success('Thank You')
           print "it worked"
           return(True)
   
class User(models.Model):
      email = models.EmailField(max_length=100)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      # *************************
      # Connect an instance of UserManager to our User model overwriting 
      # the old hidden objects key with a new one with extra properties!!!
      objects = UserManager()
