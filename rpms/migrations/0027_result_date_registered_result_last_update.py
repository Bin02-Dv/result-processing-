# Generated by Django 4.2.5 on 2023-10-03 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0026_alter_result_exam_alter_result_first_ca_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date_registered',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='result',
            name='last_update',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
