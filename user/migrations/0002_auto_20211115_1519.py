# Generated by Django 3.2.5 on 2021-11-15 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apple_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='biography',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.client'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='delux_membership',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='econtext_cus_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name_kana',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name_kanji',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_archived',
            field=models.SmallIntegerField(choices=[(0, 'Not archived'), (1, 'Archived')], default=1, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name_kana',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name_kanji',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='points_balance',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='points_reveived',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='prefecture_id',
            field=models.ForeignKey(blank=True, max_length=11, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.prefectures'),
        ),
        migrations.AlterField(
            model_name='user',
            name='remember_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='stamps_balance',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='subsequent_address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='twitter_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='zip_code',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
