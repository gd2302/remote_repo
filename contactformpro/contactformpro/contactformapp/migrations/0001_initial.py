# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-06-27 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=30)),
                ('location', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=30)),
            ],
        ),
    ]