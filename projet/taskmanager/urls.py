from django.urls import path
from . import views

urlpatterns = [
    path('projects', views.projects),
    path('project/<int:id>', views.project)
]