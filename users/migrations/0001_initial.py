# Generated by Django 3.2.9 on 2021-11-10 04:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('client_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('seconds_delivered_per_month', models.DecimalField(decimal_places=0, max_digits=15)),
                ('is_archived', models.SmallIntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prefectures',
            fields=[
                ('prefecture_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('display_order', models.SmallIntegerField()),
                ('is_default', models.SmallIntegerField(choices=[(0, 'Not default'), (1, 'Default')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_type', models.SmallIntegerField(choices=[(1, 'General user'), (2, 'Host user')], default=0)),
                ('login_type', models.CharField(choices=[('email', 'EMAIL'), ('insta', 'INSTAGRAM'), ('facebook', 'FACEBOOK'), ('twitter', 'TWITTER')], default='email', max_length=45)),
                ('email', models.CharField(max_length=254, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('remember_token', models.CharField(max_length=255, null=True)),
                ('facebook_id', models.CharField(max_length=255, null=True)),
                ('twitter_id', models.CharField(max_length=255, null=True)),
                ('apple_id', models.CharField(max_length=255, null=True)),
                ('last_name_kanji', models.CharField(max_length=255)),
                ('first_name_kanji', models.CharField(max_length=255)),
                ('last_name_kana', models.CharField(max_length=255)),
                ('first_name_kana', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('sex', models.SmallIntegerField(choices=[(0, 'Not known'), (1, 'Male'), (2, 'Female'), (9, 'Not applicable')], default=1)),
                ('is_sex_public', models.SmallIntegerField(choices=[(0, 'Private'), (1, 'Public')], default=1)),
                ('date_of_birth', models.DateField()),
                ('is_date_of_birth_public', models.SmallIntegerField(choices=[(0, 'Private'), (1, 'Public')], default=1)),
                ('phone', models.CharField(max_length=45, null=True)),
                ('zip_code', models.CharField(max_length=8, null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('subsequent_address', models.CharField(max_length=255, null=True)),
                ('biography', models.TextField(null=True)),
                ('points_balance', models.DecimalField(decimal_places=0, max_digits=15)),
                ('points_reveived', models.DecimalField(decimal_places=0, max_digits=15)),
                ('stamps_balance', models.DecimalField(decimal_places=0, max_digits=15)),
                ('econtext_cus_id', models.CharField(max_length=255, null=True)),
                ('delux_membership', models.CharField(max_length=255, null=True)),
                ('host_user_type', models.SmallIntegerField(choices=[(1, 'Individual'), (2, 'Group')], default=1, null=True)),
                ('is_authenticated', models.SmallIntegerField(choices=[(0, 'Not authenticated'), (1, 'Authenticated'), (2, 'No authenticated required')], default=1)),
                ('is_archived', models.SmallIntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.clients')),
                ('prefecture_id', models.ForeignKey(max_length=11, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.prefectures')),
            ],
        ),
    ]
