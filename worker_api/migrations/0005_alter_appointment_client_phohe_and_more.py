# Generated by Django 4.1.4 on 2022-12-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_api', '0004_remove_appointment_datetime_appointment_client_phohe_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='client_phohe',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(),
        ),
    ]
