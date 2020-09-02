from django.urls import path
from . import views

app_name = 'solution'

urlpatterns = [
    path('', views.solution_list, name='solution_list'),
    path('create_solution/', views.create_solution, name='create_solution'),
]