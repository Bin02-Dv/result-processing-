# Generated by Django 4.2.5 on 2023-10-03 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0028_result_staff_fullname_update_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='position',
            new_name='grade',
        ),
    ]
