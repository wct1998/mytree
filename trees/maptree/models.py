from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Code(models.Model):
    cid = models.IntegerField(primary_key=True)
    cno = models.IntegerField(blank=True, null=True)
    cname = models.CharField(max_length=20, blank=True, null=True)
    des = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code'


class TreeEntity(models.Model):
    id = models.IntegerField()
    entity_id = models.IntegerField(primary_key=True)
    pno = models.IntegerField()
    pname = models.CharField(max_length=20)
    p_x = models.FloatField()
    p_y = models.FloatField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dbh = models.FloatField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    plant_company = models.CharField(max_length=50, blank=True, null=True)
    plant_date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=50, blank=True, null=True)
    feature = models.CharField(max_length=50, blank=True, null=True)
    usage = models.CharField(max_length=50, blank=True, null=True)
    health = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    recorder_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    checker_id = models.IntegerField()
    check_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_entity'


class TreeSpecies(models.Model):
    pno = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=30)
    alias = models.CharField(max_length=30, blank=True, null=True)
    foreign_name = models.CharField(max_length=30, blank=True, null=True)
    latin = models.CharField(max_length=30, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    generic = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    origin = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    trait = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_species'


class TreeUser(models.Model):
    entity_id = models.IntegerField()
    pno = models.IntegerField()
    pname = models.CharField(max_length=20)
    p_x = models.FloatField()
    p_y = models.FloatField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dbh = models.FloatField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    plant_company = models.CharField(max_length=50, blank=True, null=True)
    plant_date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=50, blank=True, null=True)
    feature = models.CharField(max_length=50, blank=True, null=True)
    usage = models.CharField(max_length=50, blank=True, null=True)
    health = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    recorder_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    way = models.IntegerField(blank=True, null=True)
    checked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tree_user'


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=30, blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    upriority = models.IntegerField(blank=True, null=True)
    ucompany = models.CharField(max_length=30, blank=True, null=True)
    regist_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Code(models.Model):
    cid = models.IntegerField(primary_key=True)
    cno = models.IntegerField(blank=True, null=True)
    cname = models.CharField(max_length=20, blank=True, null=True)
    des = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code'


class TreeEntity(models.Model):
    id = models.IntegerField()
    entity_id = models.IntegerField(primary_key=True)
    pno = models.IntegerField(blank=True, null=True)
    pname = models.CharField(max_length=20, blank=True, null=True)
    p_x = models.FloatField()
    p_y = models.FloatField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dbh = models.FloatField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    plant_company = models.CharField(max_length=50, blank=True, null=True)
    plant_date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=50, blank=True, null=True)
    feature = models.CharField(max_length=50, blank=True, null=True)
    usage = models.CharField(max_length=50, blank=True, null=True)
    health = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    recorder_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    checker_id = models.IntegerField()
    check_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_entity'


class TreeSpecies(models.Model):
    pno = models.IntegerField(primary_key=True)
    pname = models.CharField(max_length=30)
    alias = models.CharField(max_length=30, blank=True, null=True)
    foreign_name = models.CharField(max_length=30, blank=True, null=True)
    latin = models.CharField(max_length=30, blank=True, null=True)
    class_field = models.CharField(db_column='class', max_length=30, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    generic = models.CharField(max_length=30, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    origin = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    trait = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tree_species'


class TreeUser(models.Model):
    entity_id = models.IntegerField()
    pno = models.IntegerField(blank=True, null=True)
    pname = models.CharField(max_length=20, blank=True, null=True)
    p_x = models.FloatField()
    p_y = models.FloatField()
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    altitude = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    dbh = models.FloatField(blank=True, null=True)
    region_id = models.IntegerField(blank=True, null=True)
    plant_company = models.CharField(max_length=50, blank=True, null=True)
    plant_date = models.DateField(blank=True, null=True)
    place = models.CharField(max_length=50, blank=True, null=True)
    rate = models.CharField(max_length=50, blank=True, null=True)
    feature = models.CharField(max_length=50, blank=True, null=True)
    usage = models.CharField(max_length=50, blank=True, null=True)
    health = models.CharField(max_length=50, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    image_id = models.IntegerField(blank=True, null=True)
    recorder_id = models.IntegerField()
    create_date = models.DateTimeField(blank=True, null=True)
    way = models.IntegerField(blank=True, null=True)
    checked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tree_user'


class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=30, blank=True, null=True)
    passport = models.CharField(max_length=20, blank=True, null=True)
    upriority = models.IntegerField(blank=True, null=True)
    ucompany = models.CharField(max_length=30, blank=True, null=True)
    regist_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
