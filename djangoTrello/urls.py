"""djangoTrello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from djangoTrello import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout_user, name='logout'),
    url(r'^authenticate/',views.authenticateUser,name='authenticate'),
    url('^change-password/$', views.change_password,{'template_name': 'changePassword.html'},),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.loginPage, name='login'),
    url(r'^app/', include('app.urls')),

]

handler404  = 'djangoTrello.views.handler404'