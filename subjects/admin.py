from django.contrib import admin

# Register your models here.
from subjects.models import Department, Subject

admin.site.register(Subject)
admin.site.register(Department)
