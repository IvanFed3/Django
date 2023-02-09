from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def user_view (request: HttpRequest, username:str) ->HttpResponse:
    return HttpResponse (f"<h1>Username: {username}</h1>")

def sum_view (_:HttpRequest, x:int, y:int) -> HttpResponse:
    return  HttpResponse (f"<p>{x}+{y} = {x+y}</p>")

def file_view (_,filepath):
    return HttpResponse(f"<p> {filepath}</p>")


def home_task1 (request:HttpRequest) -> HttpResponse:
    return HttpResponse(f"<h1>Домашня сторінка</h1>")

def home_task2 (request:HttpRequest, start:int, count:int, step:int) ->HttpResponse:
    list1 =[]
    i = 0
    while i < count:
        list1.append(start+step*i)
        i += 1
    return HttpResponse(" ".join(str(e) for e in list1))

def home_task3(request:HttpRequest, n:int):
    list1 = [0,1]
    i = 1
    while i < n:
        list1.append(list1[i]+list1[i-1])
        i += 1
    return HttpResponse(list1[n])

def home_task4(request: HttpRequest, name:str) ->HttpResponse:
    return HttpResponse (f"<p>Greeting, {name}</p>")

#Homework2
tasks = [
    {"id":1, "title":"Task #1", "complated" : False},
    {"id":2, "title":"Task #2", "complated" : False},
    {"id":3, "title":"Task #3", "complated" : False},
    {"id":4, "title":"Task #4", "complated" : False},
    {"id":5, "title":"Task #5", "complated" : False}
]

def navbar (request:HttpRequest):
    ctx = {"object_list":tasks}
    return render(request,"task_list.html", ctx)
