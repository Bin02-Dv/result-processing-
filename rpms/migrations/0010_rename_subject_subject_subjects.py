# Generated by Django 4.2.5 on 2023-09-25 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0009_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject',
            new_name='subjects',
        ),
    ]
