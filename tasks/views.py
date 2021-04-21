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
