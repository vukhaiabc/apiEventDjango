# Generated by Django 3.2.5 on 2021-11-18 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_alter_ticket_drawing_application_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='end_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='start_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]
