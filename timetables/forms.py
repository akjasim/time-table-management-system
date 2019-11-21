from django import forms

from classes.models import Class
from teachers.models import Allot


class TimeTableCreationForm(forms.Form):
    day = forms.CharField(max_length=20)
    period1 = forms.ModelChoiceField(queryset=Allot.objects.all())
    period2 = forms.ModelChoiceField(queryset=Allot.objects.all())
    period3 = forms.ModelChoiceField(queryset=Allot.objects.all())
    period4 = forms.ModelChoiceField(queryset=Allot.objects.all())
    period5 = forms.ModelChoiceField(queryset=Allot.objects.all())
    period6 = forms.ModelChoiceField(queryset=Allot.objects.all())
    period7 = forms.ModelChoiceField(queryset=Allot.objects.all())
    class_name = forms.ModelChoiceField(queryset=Class.objects.all())


class TimeTableSelectForm(forms.Form):
    class_name = forms.ModelChoiceField(queryset=Class.objects.all())