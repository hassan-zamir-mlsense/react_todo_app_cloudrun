# Generated by Django 4.1.7 on 2023-04-03 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_remove_todomodel_user_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='title',
        ),
    ]
