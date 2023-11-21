from django.http import HttpResponse
from .models import Task
from django.shortcuts import render, redirect
from .forms import TaskForm

def index(request):
    # Fetch Data From Model
    tasks = Task.objects.all()

    # Fetch Form from Forms
    form = TaskForm()

    # Insert Model Data into Template, Run Template Code, an Return to Client
    return render(request, 'index.html', {'tasks': tasks, 'form': form})

def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')  # Redirect to wherever you want after saving