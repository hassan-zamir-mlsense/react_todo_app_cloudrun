# Generated by Django 4.1.7 on 2023-03-14 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='user_name',
        ),
    ]
