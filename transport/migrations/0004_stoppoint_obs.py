# Generated by Django 2.0b1 on 2018-01-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0003_stoppoint'),
    ]

    operations = [
        migrations.AddField(
            model_name='stoppoint',
            name='obs',
            field=models.TextField(blank=True, null=True, verbose_name='Observation'),
        ),
    ]
