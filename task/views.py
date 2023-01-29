from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render
import json




tasks = [
    {"id":1, "title":"Task #1", "complated" : False},
    {"id":2, "title":"Task #2", "complated" : False},
    {"id":3, "title":"Task #3", "complated" : False},
    {"id":4, "title":"Task #4", "complated" : False},
    {"id":5, "title":"Task #5", "complated" : False}
]

def task_list_view (request:HttpRequest):
    return render(request,"./task_list.html")

def task_detail_view (request:HttpRequest, id :int) -> HttpResponse:
    for task in tasks:
        if task["id"] == id:
            return render(request,'./task_detail.html')
    raise Http404