# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    group = models.CharField(max_length=255)
    maincode = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category'


class News(models.Model):
    title = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Products(models.Model):
    group = models.CharField(max_length=255, blank=True, null=True)
    subgroup = models.CharField(max_length=255, blank=True, null=True)
    feature = models.CharField(max_length=255, blank=True, null=True)
    packaging = models.CharField(max_length=255, blank=True, null=True)
    weightvolume = models.CharField(max_length=255, blank=True, null=True)
    factory = models.CharField(max_length=255, blank=True, null=True)
    productname = models.CharField(max_length=255, blank=True, null=True)
    itemrowcode = models.CharField(max_length=255, blank=True, null=True)
    productcode = models.CharField(max_length=255, blank=True, null=True)
    itemcode = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    productitemcode = models.CharField(max_length=255, blank=True, null=True)
    category_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'