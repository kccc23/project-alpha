from django.shortcuts import render, redirect, get_object_or_404
from tasks.forms import TaskForm, NoteForm
from tasks.models import Task
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")
    else:
        form = TaskForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/create.html", context)


@login_required
def show_my_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "tasks/my_tasks.html", context)


@login_required
def add_note(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            task.note = form.cleaned_data["note"]
            task.save()
            return redirect("show_my_tasks")
    else:
        form = NoteForm()
    context = {
        "form": form,
    }
    return render(request, "tasks/note.html", context)
