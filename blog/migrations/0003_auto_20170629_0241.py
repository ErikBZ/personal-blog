# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170626_0107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_first', models.CharField(max_length=50)),
                ('author_last', models.CharField(max_length=50)),
                ('quote', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
