from django.contrib.auth.views import LoginView
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView


class CustomLoginView(LoginView):
    template_name = 'admins/login.html'

    def get_success_url(self):
        return reverse('admins:dashboard')


class DashboardView(TemplateView):
    template_name = 'admins/dashboard.html'

