# Generated by Django 4.1.7 on 2023-08-16 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0002_faculty_password_student_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='name',
            new_name='username',
        ),
    ]
