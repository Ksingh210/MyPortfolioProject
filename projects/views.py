from django.shortcuts import render
from .models import Projects

def projects(requests):
    projects = Projects.objects
    return render(requests, 'projects/projects.html', {'projects':projects})
