# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-11-04 17:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobsPosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posttitle', models.CharField(max_length=200)),
                ('postsummary', models.TextField(null=True)),
                ('postcontent', models.TextField(null=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogposts/')),
                ('authorfirstname', models.CharField(max_length=200, null=True)),
                ('authorlastname', models.CharField(max_length=200, null=True)),
                ('authorbg', models.TextField(null=True)),
                ('authordesignation', models.TextField(null=True)),
                ('authorcontact', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'JobsPosts',
            },
        ),
    ]
