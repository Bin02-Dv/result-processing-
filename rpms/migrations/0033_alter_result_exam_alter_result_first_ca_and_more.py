# Generated by Django 4.2.5 on 2023-10-08 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms', '0032_alter_result_total_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='exam',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='result',
            name='first_ca',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='result',
            name='second_ca',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
        ),
        migrations.AlterField(
            model_name='result',
            name='third_ca',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=100),
        ),
    ]