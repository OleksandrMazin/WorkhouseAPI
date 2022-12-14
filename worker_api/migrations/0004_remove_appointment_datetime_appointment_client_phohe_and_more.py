# Generated by Django 4.1.4 on 2022-12-12 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker_api', '0003_alter_appointment_datetime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='datetime',
        ),
        migrations.AddField(
            model_name='appointment',
            name='client_phohe',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
