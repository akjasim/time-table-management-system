from django.urls import path, include, reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from classes.models import Class
from subjects.models import Subject
from timetables.models import TimeTable
from . import views

app_name = 'timetables'

urlpatterns = [
    path('', views.TimeTableSelectView.as_view(), name='list'),
    path('create/', views.TimeTableAddView.as_view(), name='timetable-add')
]