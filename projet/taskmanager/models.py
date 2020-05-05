from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Project(models.Model):
    name=models.CharField(max_length=200)
    members=models.ManyToManyField(User)

    class Meta:
           verbose_name = "projet"


    def __str__(self):
           return self.name


class Status(models.Model):
    name=models.CharField(max_length=200)


    class Meta:
           verbose_name = "status"


    def __str__(self):
           return self.name



class Task(models.Model):
    project=models.ForeignKey(Project,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    assignee=models.ForeignKey(User, on_delete=models.SET_NULL,null=True )
    start_date=models.DateTimeField(default=timezone.now, verbose_name="start date")
    due_date=models.DateTimeField(default=timezone.now, verbose_name="due date")
    priority=models.IntegerField()
    status=models.ForeignKey(Status,on_delete=models.SET_NULL, null=True )

    class Meta:
           verbose_name = "task"


    def __str__(self):
           return self.name


class Journal(models.Model):
    date= models.DateTimeField(default=timezone.now, verbose_name="date")
    entry= models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.SET_NULL, null=True )
    task=models.ForeignKey(Task, on_delete=models.SET_NULL,null=True)


    class Meta:
           verbose_name = "journal"



    def __str__(self):
           return self.entry