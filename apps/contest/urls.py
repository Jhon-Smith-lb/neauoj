from django.urls import path
from . import views

app_name = 'contest'

urlpatterns = [
    path('', views.contests_list, name='contests_list'),
    path('<int:contest_id>/', views.contest_detail, name="contest_detail"),
]