# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('thaifood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('healing_element', models.ForeignKey(to='thaifood.Element', null=True)),
            ],
            options={
                'verbose_name': '\u0e40\u0e0a\u0e37\u0e49\u0e2d\u0e42\u0e23\u0e04',
                'verbose_name_plural': '\u0e01\u0e25\u0e38\u0e48\u0e21\u0e40\u0e0a\u0e37\u0e49\u0e2d\u0e42\u0e23\u0e04',
            },
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': '\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48\u0e2d\u0e32\u0e2b\u0e32\u0e23',
                'verbose_name_plural': '\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48\u0e2d\u0e32\u0e2b\u0e32\u0e23',
            },
        ),
        migrations.CreateModel(
            name='IngredientCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
            ],
            options={
                'verbose_name': '\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48\u0e27\u0e31\u0e15\u0e16\u0e38\u0e14\u0e34\u0e1a',
                'verbose_name_plural': '\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2b\u0e21\u0e27\u0e14\u0e2b\u0e21\u0e39\u0e48\u0e27\u0e31\u0e15\u0e16\u0e38\u0e14\u0e34\u0e1a',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.DecimalField(max_digits=14, decimal_places=4)),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('water', models.DecimalField(max_digits=14, decimal_places=4)),
                ('protein', models.DecimalField(max_digits=14, decimal_places=4)),
                ('fat', models.DecimalField(max_digits=14, decimal_places=4)),
                ('carbohydrate', models.DecimalField(max_digits=14, decimal_places=4)),
                ('dietary_fiber', models.DecimalField(max_digits=14, decimal_places=4)),
                ('ash', models.DecimalField(max_digits=14, decimal_places=4)),
                ('calcium', models.DecimalField(max_digits=14, decimal_places=4)),
                ('phosphorus', models.DecimalField(max_digits=14, decimal_places=4)),
                ('iron', models.DecimalField(max_digits=14, decimal_places=4)),
                ('retinol', models.DecimalField(max_digits=14, decimal_places=4)),
                ('beta_carotene', models.DecimalField(max_digits=14, decimal_places=4)),
                ('vitamin_A', models.DecimalField(max_digits=14, decimal_places=4)),
                ('vitaminE', models.DecimalField(max_digits=14, decimal_places=4)),
                ('thiamin', models.DecimalField(max_digits=14, decimal_places=4)),
                ('riboflavin', models.DecimalField(max_digits=14, decimal_places=4)),
                ('niacin', models.DecimalField(max_digits=14, decimal_places=4)),
                ('vitamin_C', models.DecimalField(max_digits=14, decimal_places=4)),
            ],
            options={
                'verbose_name': '\u0e2a\u0e32\u0e23\u0e2d\u0e32\u0e2b\u0e32\u0e23',
                'verbose_name_plural': '\u0e01\u0e25\u0e38\u0e48\u0e21\u0e2a\u0e32\u0e23\u0e2d\u0e32\u0e2b\u0e32\u0e23',
            },
        ),
        migrations.AddField(
            model_name='food',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='description',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='element',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='thaifood.Element', null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu',
            name='food',
            field=models.ForeignKey(to='thaifood.Food'),
        ),
        migrations.AddField(
            model_name='menu',
            name='ingredient',
            field=models.ForeignKey(to='thaifood.Ingredient'),
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ManyToManyField(to='thaifood.FoodCategory'),
        ),
        migrations.AddField(
            model_name='food',
            name='ingredients',
            field=models.ManyToManyField(to='thaifood.Ingredient', through='thaifood.Menu'),
        ),
        migrations.AddField(
            model_name='food',
            name='nutrient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='thaifood.Nutrient', null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='affect',
            field=models.ManyToManyField(related_name='affect', to='thaifood.Disease'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='category',
            field=models.ManyToManyField(to='thaifood.IngredientCategory'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='healing',
            field=models.ManyToManyField(related_name='healing', to='thaifood.Disease'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='nutrient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='thaifood.Nutrient', null=True),
        ),
    ]
