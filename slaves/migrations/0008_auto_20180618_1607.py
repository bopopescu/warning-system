# Generated by Django 2.0.5 on 2018-06-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slaves', '0007_threshold_multiplication_factor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threshold',
            name='multiplication_factor',
        ),
        migrations.AddField(
            model_name='sensor',
            name='multiplication_factor',
            field=models.FloatField(default=1),
        ),
    ]
