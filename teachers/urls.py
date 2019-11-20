from django.urls import path, reverse_lazy
from django.views.generic import ListView, CreateView

from teachers.models import Teacher

app_name = 'teachers'

urlpatterns = [
    path('', ListView.as_view(model=Teacher), name='list'),
    path('create/', CreateView.as_view(model=Teacher, fields='__all__',
                                       success_url=reverse_lazy('admins:teachers:list')), name='create'),
]
