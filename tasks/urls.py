from django.urls import path
from tasks.views import create_task, show_my_tasks, add_note

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_my_tasks, name="show_my_tasks"),
    path("<int:id>/", add_note, name="add_note"),
]
