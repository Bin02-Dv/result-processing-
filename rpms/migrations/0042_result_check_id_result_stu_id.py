# Generated by Django 4.2.5 on 2023-10-10 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0041_remove_result_check_id_remove_result_stu_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='check_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='result',
            name='stu_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
