# Generated by Django 4.2.5 on 2023-10-08 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0031_remove_result_student_name_reportcard_stu_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='total_marks',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
