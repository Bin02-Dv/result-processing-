# Generated by Django 4.2.5 on 2023-10-07 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0030_reportcard'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='student_name',
        ),
        migrations.AddField(
            model_name='reportcard',
            name='stu_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='rpms.student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='stu_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rpms.student'),
        ),
    ]
