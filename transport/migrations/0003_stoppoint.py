# Generated by Django 2.0b1 on 2017-11-07 10:30

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='StopPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(-22.99977, -43.36063), srid=4326, verbose_name='Location')),
            ],
            options={
                'verbose_name': 'StopPoint',
                'verbose_name_plural': 'StopPoints',
            },
        ),
    ]
