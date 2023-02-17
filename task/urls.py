from django.urls import path
from task.views import task_view, task_detail_view

urlpatterns = [

    path ('', task_view, name = "tasks"),
    path('<int:id>', task_detail_view, name = "task")

]
