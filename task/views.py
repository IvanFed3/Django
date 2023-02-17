from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
from task.models import Task



# def navbar (request:HttpRequest):
#     ctx = {"object_list":tasks}
#     return render(request,"task_list.html", ctx)

tasks = Task.objects.all()
ctx = {"tasks": tasks}

def task_detail_view (request:HttpRequest, id :int) -> HttpResponse:
    for task in tasks:
        if task.id == id:
            ctx = {"task": task}
            return render(request,'task_detail.html', ctx)
    raise Http404

def task_view (request:HttpRequest):
    return render(request, 'task.html', ctx)