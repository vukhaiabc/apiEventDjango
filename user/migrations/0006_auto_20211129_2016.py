# Generated by Django 3.2.5 on 2021-11-29 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20211129_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='city',
        ),
        migrations.RemoveField(
            model_name='user',
            name='points_reveived',
        ),
        migrations.RemoveField(
            model_name='user',
            name='stamps_balance',
        ),
    ]
