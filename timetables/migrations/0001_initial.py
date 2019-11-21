# Generated by Django 2.1.4 on 2019-11-21 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=50)),
                ('period1', models.CharField(max_length=50)),
                ('period2', models.CharField(max_length=50)),
                ('period3', models.CharField(max_length=50)),
                ('period4', models.CharField(max_length=50)),
                ('period5', models.CharField(max_length=50)),
                ('period6', models.CharField(max_length=50)),
                ('period7', models.CharField(max_length=50)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='classes.Class')),
            ],
        ),
    ]
