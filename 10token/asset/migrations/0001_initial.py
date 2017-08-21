# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-19 21:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Token name')),
                ('amount', models.CharField(max_length=100, verbose_name='Amount')),
                ('description', models.TextField(verbose_name='Description')),
                ('reissuable', models.BooleanField()),
                ('token_id', models.CharField(max_length=100, verbose_name='Token id')),
                ('sender_id', models.CharField(max_length=100, verbose_name='Sender id')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
