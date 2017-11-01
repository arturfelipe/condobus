# Generated by Django 2.0b1 on 2017-11-01 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('org', '0002_auto_20171030_0305'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buses', to='org.Organization', verbose_name='Organization')),
            ],
            options={
                'verbose_name': 'Bus',
                'verbose_name_plural': 'Buses',
            },
        ),
    ]