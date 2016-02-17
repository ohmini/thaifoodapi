##-*-coding: utf-8 -*-
from django.db import models


class Element(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ธาตุ"
        verbose_name_plural = "ธาตุต่างๆ"


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "วัตถุดิบ"
        verbose_name_plural = "กลุ่มวัตถุดิบ"


class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    calories = models.IntegerField()

    class Meta:
        verbose_name = "อาหาร"
        verbose_name_plural = "กลุ่มอาหาร"
