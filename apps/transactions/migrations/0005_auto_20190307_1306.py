# Generated by Django 2.1.7 on 2019-03-07 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0004_auto_20190307_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='key',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='value',
            field=models.CharField(max_length=500),
        ),
    ]
