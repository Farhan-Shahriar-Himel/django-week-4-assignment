# Generated by Django 5.0.2 on 2024-03-04 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskCategory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskcategory',
            name='taskModel',
        ),
    ]