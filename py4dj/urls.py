"""py4dj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from task.views import task_detail_view, task_list_view



urlpatterns = [

    # Homework1
    path("homepage/", views.home_task1),
    path("home/", views.home_task1),
    path("", views.home_task1),
    path("progression/<int:start>/<int:count>/<int:step>/", views.home_task2),
    path("fib/<int:n>", views.home_task3),
    path ('greeting/<str:name>/', views.home_task4),

    path("files/<path:filepath>", views.file_view),
    path('sum_num/<int:x>/<int:y>/', views.sum_view), #< int, str, slug, uid, path : argument> slug - стрічка, яка містить a-z, 0-1, _ path - теж стрічка, але може містити "/"
    path ('users/<str:username>/', views.user_view),
    path('admin/', admin.site.urls), #path/re_path ("route",  view, Optional [name])


    path('task/', include('task.urls'))


]
