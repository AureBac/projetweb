from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from taskmanager.models import Project, Task, Journal
# Create your views here.
@login_required()
def projects(request):
    projects=Project.objects.filter(members__username=request.user.username)
    return render(request, 'projects.html', {'projects':projects})


@login_required()
def project(request, id):
    projectlist=Project.objects.filter(id=id)
    tasks=Task.objects.filter(project_id=id)
    return render(request, 'project.html',{'projectlist':projectlist,'tasks':tasks })


@login_required()
def task(request, id_task,id_project):
    tasklist=Task.objects.filter(id=id_task)
    entrylist=Journal.objects.filter(task_id=id_task)
    projectlist = Project.objects.filter(id=id_project)
    return render(request,'task.html',{'tasklist':tasklist, 'entrylist':entrylist, 'projectlist':projectlist})

