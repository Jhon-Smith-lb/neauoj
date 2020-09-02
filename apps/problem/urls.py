from django.urls import path
from . import views

app_name = 'problem'

urlpatterns = [
    path('', views.problems_list, name='problems_list'),
    path('<int:problem_id>/', views.problem_detail, name="problem_detail"),
]