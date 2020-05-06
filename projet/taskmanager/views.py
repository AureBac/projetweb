from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from taskmanager.models import Project, Task
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
