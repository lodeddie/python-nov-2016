from __future__ import unicode_literals

from django.db import models

from ..login_registration_app.models import User

# Create your models here.

class Blog(models.Model):
      title = models.CharField(max_length=50)
      blog = models.TextField(max_length=500)
      blog_creator = models.ForeignKey(User)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)