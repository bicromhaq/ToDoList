from django.shortcuts import render
from . import models
from home.models import Task

# Create your views here.

def home(request):
    context ={'success':False}
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(title=title, description=desc)
        ins.save()
        context ={'success':True}
    
    return render(request, 'base.html')

def task(request):
    allTask = Task.objects.all()
    context = {'tasks': allTask}
    return render(request, 'task.html', context)

def delete_task(request, id):
    std = models.Task.objects.get(pk=id)
    print(std)