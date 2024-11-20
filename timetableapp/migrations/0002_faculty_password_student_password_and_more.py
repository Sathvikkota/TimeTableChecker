# Generated by Django 4.1.7 on 2023-08-16 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='password',
            field=models.CharField(default='klu123', max_length=30),
        ),
        migrations.AddField(
            model_name='student',
            name='password',
            field=models.CharField(default='klu123', max_length=30),
        ),
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(default='klu123', max_length=128),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('Cse-H', 'CSE-H'), ('Cse', 'CSE'), ('Csit', 'CSIT'), ('Aids', 'AIDS'), ('Ece', 'ECE'), ('Eee', 'EEE'), ('BBA', 'BBA'), ('Mechanical', 'Mechanical'), ('Biotechnology', 'Biotechnology'), ('Civil', 'Civil'), ('Mba', 'MBA'), ('B.arch', 'B.Arch')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(choices=[('associate_professor', 'Associate Professor'), ('professor', 'Professor'), ('assistant_professor', 'Assistant Professor'), ('lecturer', 'Lecturer')], default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(choices=[('M.Tech', 'M.TECH'), ('PhD', 'PhD'), ('Masters', "Master's"), ('Msc', 'M.Sc'), ('Bsc', 'B.Sc'), ('Bed', 'B.Ed')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('Cse-H', 'CSE-H'), ('Cse', 'CSE'), ('Csit', 'CSIT'), ('Aids', 'AIDS'), ('Ece', 'ECE'), ('Eee', 'EEE'), ('BBA', 'BBA'), ('Mechanical', 'Mechanical'), ('Biotechnology', 'Biotechnology'), ('Civil', 'Civil'), ('Mba', 'MBA'), ('B.arch', 'B.Arch')], default=None, max_length=50),
        ),
    ]