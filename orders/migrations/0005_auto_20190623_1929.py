# Generated by Django 2.2.2 on 2019-06-24 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20190623_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='gardensoilpallets',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='order',
            name='pottingmixpallets',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AddField(
            model_name='order',
            name='raisedbedpallets',
            field=models.CharField(default=0, max_length=2),
        ),
    ]
