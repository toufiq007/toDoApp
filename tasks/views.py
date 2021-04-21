from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.


def index(request):
    task = Task.objects.all()
    form = Taskform()

    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form,'tasks':task}
    return render(request,'tasks/base.html',context)



def update_file(request,pk):
    task = Task.objects.get(id=pk)
    form = Taskform(instance=task)

    if request.method == "POST":
        form  = Taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}

    return render(request,'tasks/update.html',context)
