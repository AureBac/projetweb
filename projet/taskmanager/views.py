from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from taskmanager.models import Project
# Create your views here.
@login_required()
def projects(request):
    #args={'user':request.user}
    projects=Project.objects.filter(members__username=request.user.username)
    #return render(request, 'projects.html', args)
    return render(request, 'projects.html', {'projects':projects})