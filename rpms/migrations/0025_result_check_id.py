# Generated by Django 4.2.5 on 2023-10-02 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0024_alter_result_exam_alter_result_first_ca_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='check_id',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]