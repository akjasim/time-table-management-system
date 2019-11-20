from django.contrib.auth.views import LoginView
from django.urls import path, include
from . import views

app_name = 'admins'

urlpatterns = [
    path('', views.CustomLoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('subjects/', include('subjects.urls')),
    path('classes/', include('classes.urls')),
    path('teachers/', include('teachers.urls')),
]
