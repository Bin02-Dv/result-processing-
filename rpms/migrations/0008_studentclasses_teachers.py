# Generated by Django 4.2.5 on 2023-09-24 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0007_studentclasses'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentclasses',
            name='teachers',
            field=models.TextField(blank=True, max_length=50000),
        ),
    ]
