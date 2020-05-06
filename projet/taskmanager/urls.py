from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.projects),
    path('project/<int:id>', views.project),
    path('task/<int:id_task>/<int:id_project>', views.task),
]