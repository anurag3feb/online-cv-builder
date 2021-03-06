# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-09 05:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_educationdetails_intership_job_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraduationDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(default='', max_length=50)),
                ('board', models.CharField(default='', max_length=20)),
                ('cgpa', models.FloatField(default=0)),
                ('year', models.CharField(default='', max_length=20)),
                ('course', models.CharField(choices=[('bsc', 'B.Sc.'), ('be', 'B.E.'), ('btech', 'B.Tech.'), ('ba', 'B.A.'), ('bcom', 'B.Com.')], max_length=20)),
                ('stream', models.CharField(choices=[('it', 'Information Technology'), ('cs', 'Computer Science'), ('mech', 'Mechanical Engg'), ('ee', 'Electrical Engg'), ('ece', 'Electronics and Communication'), ('history', 'History'), ('geography', 'Geography'), ('economics', 'Economics'), ('physics', 'Physics'), ('chemistry', 'Chemistry'), ('maths', 'Maths')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SeniorSecondaryDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolName', models.CharField(default='', max_length=50)),
                ('board', models.CharField(default='', max_length=20)),
                ('cgpa', models.FloatField(default=0)),
                ('year', models.CharField(default='', max_length=20)),
                ('stream', models.CharField(choices=[('art', 'Arts'), ('commerce', 'Commerce'), ('science', 'Science')], max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='EducationDetails',
            new_name='SecondaryDetails',
        ),
    ]
