# Generated by Django 4.2 on 2023-04-21 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]