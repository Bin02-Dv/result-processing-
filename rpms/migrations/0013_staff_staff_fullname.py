# Generated by Django 4.2.5 on 2023-09-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0012_studentclasses_teachers_usernames'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_fullname',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
