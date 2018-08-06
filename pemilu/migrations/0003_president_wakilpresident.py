# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-08-05 09:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pemilu', '0002_auto_20180805_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='President',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemilu.Person')),
            ],
        ),
        migrations.CreateModel(
            name='WakilPresident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cawapress', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pemilu.Person')),
            ],
        ),
    ]
