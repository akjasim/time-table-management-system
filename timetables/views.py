from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import View, TemplateView

from classes.models import Class
from teachers.models import Allot
from timetables.forms import TimeTableCreationForm, TimeTableSelectForm
from timetables.models import TimeTable


class TimeTableAddView(View):
    def get(self, *args, **kwargs):
        form = TimeTableCreationForm()
        print(form)
        allots = Allot.objects.all()
        return render(self.request, 'timetables/timetable_form.html', {'form': form})

    def post(self, *kwargs):
        form = TimeTableCreationForm(self.request.POST)
        if form.is_valid():
            TimeTable.objects.create(**form.cleaned_data)
        return redirect('admins:timetables:list')


class TimeTableSelectView(View):
    def get(self, *args, **kwargs):
        if self.request.GET.get('class_name'):
            form = TimeTableSelectForm(self.request.GET)
            if form.is_valid():
                timetable = TimeTable.objects.all().filter(class_name=form.cleaned_data.get('class_name'))
                return render(self.request, 'timetables/timetable_select.html', {'timetable': timetable})
        form = TimeTableSelectForm()
        extra_context = {'classes': Class.objects.all(), 'form': form}
        return render(self.request, 'timetables/timetable_select.html', extra_context)