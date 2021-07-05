from django.shortcuts import render
from work.models import Project

def work_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'work_index.html', context)

def work_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'work_detail.html', context)
