# Generated by Django 5.1.6 on 2025-02-24 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P1', '0005_notifications_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Semester',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='P1.sem'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='notifications',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='P1.sem'),
        ),
    ]
