# Generated by Django 3.2.5 on 2021-11-29 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20211129_2013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='delux_membership',
        ),
        migrations.RemoveField(
            model_name='user',
            name='econtext_cus_id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subsequent_address',
        ),
    ]
