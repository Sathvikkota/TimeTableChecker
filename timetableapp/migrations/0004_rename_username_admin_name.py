# Generated by Django 4.1.7 on 2023-08-16 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0003_rename_name_admin_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='username',
            new_name='name',
        ),
    ]
