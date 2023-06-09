# Generated by Django 4.1.7 on 2023-03-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, null=True)),
                ('title', models.CharField(default='New-Todo', max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
