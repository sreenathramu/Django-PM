import requests
from django.http import HttpResponseRedirect

class LoginValidatorMiddleware(object):

	def __init__(self,get_response):
		self.get_response = get_response

	def __call__(self,request):
		if not request.user.is_authenticated():
			return HttpResponseRedirect('login')
		response = self.get_response(request)
		return response