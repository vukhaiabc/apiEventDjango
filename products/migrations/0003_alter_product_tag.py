# Generated by Django 3.2.5 on 2021-11-29 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211129_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.ManyToManyField(blank=True, to='products.Tag'),
        ),
    ]
