from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
from task.models import Task


tasks = Task.objects.all()
ctx = {"tasks": tasks}
def register (request:HttpRequest):
    return render(request,"register.html", ctx)

def login (request:HttpRequest):
    return render(request,"login.html",ctx)
