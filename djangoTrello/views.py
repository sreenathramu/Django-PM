from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.http import *
import ntpath
import os.path
from django.template import RequestContext
from forms import SignUpForm
# Create your views here.

def loginPage(request):
    # raise Http404("404.HTML")
    return  render(request,'login.html')
def logout_user(request):
    logout(request)
    return redirect('/')

def authenticateUser(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/app/home')
        else:
            return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def change_password(request):
    template_response = views.password_change(request)
    return template_response

def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response
