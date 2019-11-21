from django.db import models

# Create your models here.
from subjects.models import Department, Subject


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Allot(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher.name}-{self.subject.name}'
