# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from models import *
from forms import CategoryAddForm
from django.forms import inlineformset_factory
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.decorators import login_required

@login_required
def main(request):	
	try:
		if request.method == 'POST':
			form = CategoryAddForm(request.POST)
			if form.is_valid():
				form.save()
			form =  CategoryAddForm()
			messages.info(request, 'Category Successfully Added')
		else:
			form = CategoryAddForm()
	except Exception as e:
		raise Http404(e)
	category = Category.objects.all()
	return render(request,'category.html',{'category':category,'form':form})

@login_required
def category_get(request,categoryId):
	try:
		user = User.objects.get(username=request.user)
		category = Category.objects.get(pk=categoryId)
		tasks = Tasks.objects.filter(category=categoryId,user=user)
		categoryList = Category.objects.all()
		if request.method == 'POST':
			task = Tasks()
			task.task_title = request.POST['task_title'] 
			task.task_description = request.POST['task_description'] 
			task.category= category
			task.user = user
			task.save()
			messages.info(request, 'Task Successfully Added')
	except Exception as e:
		raise Http404(e)
	return render(request,'tasks.html',{'task':tasks,'category':category,
		'user':user,
		'categoryList':categoryList})

@login_required
def deleteTask(request,taskId):
	try:
		task  = Tasks.objects.get(id=taskId)
		task.delete()
		messages.info(request, 'Task Successfully Deleted')
	except Exception as e:
		raise Http404(e)
	return redirect('getCategory')

@login_required
def deleteCategory(request,categoryId):
	try:
		category  = Category.objects.get(id=categoryId)
		category.delete()
		messages.info(request, 'Category Successfully Deleted')
	except Exception as e:
		raise Http404(e)
	return redirect('home')

@login_required
def moveTask(request):
	try:
		taskId = request.POST['taskHiddenId']
		currentCategoryId = request.POST['categoryHiddenId']
		categoryId = request.POST['category']
		taskObj = Tasks.objects.filter(id=taskId)
		categoryObj = Category.objects.get(pk=categoryId)
		taskObj.update(category = categoryObj)
		messages.info(request, 'Task updated Successfully')
	except Exception as e:
		raise Http404('e')
	return redirect('getCategory',categoryId=currentCategoryId)

