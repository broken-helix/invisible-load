# Generated by Django 5.0.4 on 2024-04-25 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0010_task_completed_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
