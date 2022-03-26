from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm
from .utils import searchProjects


def projects(request):
    projects, search_query = searchProjects(request)
    context = {"projects": projects, 'search_query': search_query}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {"project": project}
    return render(request, 'projects/single-project.html', context)


@login_required(login_url='login')
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            messages.success(request, 'Project created successfully')
            return redirect('account')

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid:
            form.save()
            messages.success(request, 'Project updated successfully')
            return redirect("account")

    context = {'form': form}
    return render(request, 'projects/project_form.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully')
        return redirect('account')

    context = {'object': project}
    return render(request, 'users/delete.html', context)
