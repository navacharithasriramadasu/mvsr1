# Generated by Django 5.1.6 on 2025-03-01 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P1', '0008_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notifications',
            name='semester',
            field=models.IntegerField(),
        ),
    ]
