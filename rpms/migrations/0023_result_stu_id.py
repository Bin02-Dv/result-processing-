# Generated by Django 4.2.5 on 2023-10-02 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0022_result_third_ca'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='stu_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
