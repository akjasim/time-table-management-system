from django.urls import path, include, reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from classes.models import Class
from subjects.models import Subject
from . import views

app_name = 'classes'

urlpatterns = [
    path('', ListView.as_view(model=Class), name='list'),
    path('create/', CreateView.as_view(model=Class, fields='__all__',
                                       success_url=reverse_lazy('admins:classes:list')), name='create'),
]