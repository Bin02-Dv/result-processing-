# Generated by Django 4.2.5 on 2023-10-08 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0034_alter_result_exam_alter_result_first_ca_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='staff_fullname_update',
        ),
        migrations.RemoveField(
            model_name='result',
            name='staff_role_update',
        ),
        migrations.RemoveField(
            model_name='result',
            name='staff_username_update',
        ),
    ]
