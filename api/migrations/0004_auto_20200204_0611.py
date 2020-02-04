# Generated by Django 2.2.8 on 2020-02-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200201_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='furniture',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.PositiveIntegerField(),
        ),
    ]
