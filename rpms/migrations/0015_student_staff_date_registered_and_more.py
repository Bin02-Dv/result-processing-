# Generated by Django 4.2.5 on 2023-10-01 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0014_studentclasses_term'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(blank=True, max_length=100)),
                ('f_name', models.CharField(blank=True, max_length=100)),
                ('l_name', models.CharField(blank=True, max_length=100)),
                ('m_name', models.CharField(blank=True, max_length=100)),
                ('dob', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=100)),
                ('class_name', models.CharField(blank=True, max_length=100)),
                ('term', models.CharField(blank=True, max_length=100)),
                ('stu_address', models.TextField(blank=True, max_length=50000)),
                ('g_fullname', models.CharField(blank=True, max_length=100)),
                ('g_phone_number', models.CharField(blank=True, max_length=100)),
                ('g_address', models.CharField(blank=True, max_length=100)),
                ('relationship', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('date_registered', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='date_registered',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='studentclasses',
            name='date_registered',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='subject',
            name='date_registered',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
