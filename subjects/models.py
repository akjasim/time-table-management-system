from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20)
    semester = models.CharField(max_length=2)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
