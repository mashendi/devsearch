from multiprocessing import context
from django.shortcuts import render
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, 'projects/single-project.html', context)
