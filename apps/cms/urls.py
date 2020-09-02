from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.users_list, name='users_list'),
    path('create_problem/', views.create_problem, name='create_problem'),
    path('create_contest/', views.create_contest, name='create_contest'),
    path('create_contest_problem/', views.create_contest_problem, name='create_contest_problem'),
]