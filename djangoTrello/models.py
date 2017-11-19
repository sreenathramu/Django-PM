from __future__ import unicode_literals
from datetime import  datetime
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
import uuid

class User(models.Model):
    first_name=models.CharField(max_length=160)
    last_name=models.CharField(max_length=160)
    username=models.CharField(max_length=160)
    email=models.CharField(max_length=160)
    class Meta:
        managed=False
        db_table='auth_user'
        ordering =['first_name']