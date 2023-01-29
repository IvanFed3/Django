
from django.urls import path
from task.views import task_detail_view, task_list_view

urlpatterns = [

    path ('', task_list_view),
    path('<int:id>', task_detail_view)

]
