# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': '\u0e18\u0e32\u0e15\u0e38',
                'verbose_name_plural': '\u0e18\u0e32\u0e15\u0e38\u0e15\u0e48\u0e32\u0e07\u0e46',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('calories', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u0e2d\u0e32\u0e2b\u0e32\u0e23',
                'verbose_name_plural': '\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2d\u0e32\u0e2b\u0e32\u0e23',
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('calories', models.IntegerField()),
            ],
            options={
                'verbose_name': '\u0e27\u0e31\u0e15\u0e16\u0e38\u0e14\u0e34\u0e1a',
                'verbose_name_plural': '\u0e01\u0e25\u0e38\u0e48\u0e21\u0e27\u0e31\u0e15\u0e16\u0e38\u0e14\u0e34\u0e1a',
            },
        ),
    ]
