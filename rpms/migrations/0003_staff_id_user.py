# Generated by Django 4.2.5 on 2023-09-15 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0002_alter_staff_staff_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='id_user',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
