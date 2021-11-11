# Generated by Django 3.2.5 on 2021-11-11 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_users_prefecture_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Box_notification_trans_content',
            fields=[
                ('box_notification_trans_content_id', models.AutoField(primary_key=True, serialize=False)),
                ('from_type', models.IntegerField(choices=[(1, 'Host user'), (2, 'Client user (Mgmt portal user)'), (3, 'System admin user( Mgmt portal user)')], default=1)),
                ('from_user_id', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('to_user_ids', models.TextField(null=True)),
                ('scheduled_at', models.DateTimeField(auto_now_add=True)),
                ('is_delivered', models.IntegerField(choices=[(0, 'Not delivered'), (1, 'Delivered')])),
                ('delivered_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='clients',
            name='client_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Image_paths',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=255)),
                ('dir_path', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('display_order', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('box_notification_trans_content_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.box_notification_trans_content')),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.clients')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
        migrations.AddField(
            model_name='box_notification_trans_content',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.clients'),
        ),
    ]
