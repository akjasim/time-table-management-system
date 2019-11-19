from django.contrib.auth.views import LoginView
from django.urls import path, include, reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView

from subjects.models import Subject
from . import views

app_name = 'subjects'

urlpatterns = [
    path('', ListView.as_view(model=Subject), name='list'),
    path('create/', CreateView.as_view(model=Subject, fields='__all__',
                                       success_url=reverse_lazy('admins:subjects:list')), name='create'),
]
