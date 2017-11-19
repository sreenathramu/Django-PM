from django.conf.urls import url
from app import views

urlpatterns = [
	url(r'^home$',views.main,name="home"),
	url(r'^category/(?P<categoryId>[0-9]+)$',views.category_get,name="getCategory"),
	url(r'^delete/category/(?P<categoryId>[0-9]+)$',views.deleteCategory,name="categoryTask"),
	url(r'^delete/task/(?P<taskId>[0-9]+)$',views.deleteTask,name="deleteTask"),
	url(r'^move$',views.moveTask,name="moveTask")
]