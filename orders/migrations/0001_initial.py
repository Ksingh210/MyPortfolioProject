# Generated by Django 2.2.2 on 2019-06-23 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.CharField(max_length=100)),
                ('time', models.DateTimeField()),
                ('item1', models.BooleanField()),
                ('item2', models.BooleanField()),
                ('item3', models.BooleanField()),
            ],
        ),
    ]