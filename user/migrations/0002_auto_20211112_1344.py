# Generated by Django 3.2.5 on 2021-11-12 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_event_client_id'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_paths',
            name='box_notification_trans_content_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.box_notification_trans_content'),
        ),
        migrations.AlterField(
            model_name='image_paths',
            name='event_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='event.event'),
        ),
        migrations.AlterField(
            model_name='image_paths',
            name='user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user'),
        ),
    ]
