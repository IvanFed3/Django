from django.db import models

class Task(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    completed = models.BooleanField()



