from django.db import models

# Create your models here.
from classes.models import Class
from teachers.models import Allot


class TimeTable(models.Model):
    day = models.CharField(max_length=50)
    period1 = models.CharField(max_length=50)
    period2 = models.CharField(max_length=50)
    period3 = models.CharField(max_length=50)
    period4 = models.CharField(max_length=50)
    period5 = models.CharField(max_length=50)
    period6 = models.CharField(max_length=50)
    period7 = models.CharField(max_length=50)
    class_name = models.ForeignKey(Class, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.day}-{self.class_name.name}'
