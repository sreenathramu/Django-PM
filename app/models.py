# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime   
from djangoTrello.models import User

# Create your models here.
class Category(models.Model):
	category_name = models.CharField(max_length=50)
	description   = models.CharField(max_length=250)
	created_date  = models.DateTimeField(default=datetime.now) 

	class Meta:
		ordering = ['created_date']

class Tasks(models.Model):
	task_title = models.CharField(max_length=50)
	task_description = models.CharField(max_length=200)
	category = models.ForeignKey(Category,on_delete = models.CASCADE,related_name='from_category',)
	user = models.ForeignKey(User,related_name='from_user',)
	priority = models.IntegerField()
	created_date  = models.DateTimeField(default=datetime.now) 

	class Meta:
		ordering = ['created_date']