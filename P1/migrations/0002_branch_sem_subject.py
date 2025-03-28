# Generated by Django 5.1.6 on 2025-02-23 15:29

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('P1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Sem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(8)])),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='P1.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=60)),
                ('subject_code', models.CharField(max_length=10)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='P1.sem')),
            ],
        ),
    ]
