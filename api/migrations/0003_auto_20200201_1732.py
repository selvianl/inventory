# Generated by Django 2.2.8 on 2020-02-01 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200130_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
