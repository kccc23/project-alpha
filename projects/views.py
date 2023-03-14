from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from projects.models import Project, Company
from projects.forms import ProjectForm
import pandas
import plotly.express as px
from plotly.offline import plot

# Create your views here.


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)

@login_required
def show_project(request, id):
    project = get_object_or_404(Project, id=id)
    context = {
        "project": project,
    }
    return render(request, "projects/detail.html", context)

@login_required
def show_company(request, id):
    company = get_object_or_404(Company, id=id)
    context = {
        "company": company,
    }
    return render(request, "companies/detail.html", context)

@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
    context = {
        "form": form,
    }
    return render(request, "projects/create.html", context)

@login_required
def view_timeline(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = project.tasks.all()
    data = [
        {
            "Task": task.name,
            "Start": task.start_date,
            "Due": task.due_date,
            "Assignee": task.assignee
        } for task in tasks
    ]
    df = pandas.DataFrame(data)
    fig = px.timeline(
        df, x_start="Start", x_end="Due",
        y="Task", color="Assignee"
    )
    fig.update_yaxes(autorange="reversed")
    gantt_plot = plot(fig, output_type="div")
    context = {
        "plot_div": gantt_plot
    }
    return render(request, "projects/time.html", context)