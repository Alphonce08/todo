# Generated by Django 4.2 on 2023-04-21 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_todo_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='complete_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
