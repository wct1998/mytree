from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
# from django.db import models
#
#
# class Code(models.Model):
#     cid = models.IntegerField(primary_key=True)
#     cno = models.IntegerField(blank=True, null=True)
#     cname = models.CharField(max_length=20, blank=True, null=True)
#     des = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'code'
#
#
# class TreeEntity(models.Model):
#     id = models.IntegerField()
#     entity_id = models.IntegerField(primary_key=True)
#     pno = models.IntegerField()
#     pname = models.CharField(max_length=20)
#     p_x = models.FloatField()
#     p_y = models.FloatField()
#     longitude = models.FloatField(blank=True, null=True)
#     latitude = models.FloatField(blank=True, null=True)
#     altitude = models.FloatField(blank=True, null=True)
#     height = models.FloatField(blank=True, null=True)
#     dbh = models.FloatField(blank=True, null=True)
#     region_id = models.IntegerField(blank=True, null=True)
#     plant_company = models.CharField(max_length=50, blank=True, null=True)
#     plant_date = models.DateField(blank=True, null=True)
#     place = models.CharField(max_length=50, blank=True, null=True)
#     rate = models.CharField(max_length=50, blank=True, null=True)
#     feature = models.CharField(max_length=50, blank=True, null=True)
#     usage = models.CharField(max_length=50, blank=True, null=True)
#     health = models.CharField(max_length=50, blank=True, null=True)
#     introduction = models.TextField(blank=True, null=True)
#     gender = models.CharField(max_length=4, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     image_id = models.IntegerField(blank=True, null=True)
#     recorder_id = models.IntegerField()
#     create_date = models.DateTimeField(blank=True, null=True)
#     checker_id = models.IntegerField()
#     check_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tree_entity'
#
#
# class TreeSpecies(models.Model):
#     pno = models.IntegerField(primary_key=True)
#     pname = models.CharField(max_length=30)
#     alias = models.CharField(max_length=30, blank=True, null=True)
#     foreign_name = models.CharField(max_length=30, blank=True, null=True)
#     latin = models.CharField(max_length=30, blank=True, null=True)
#     class_field = models.CharField(db_column='class', max_length=30, blank=True,
#                                    null=True)  # Field renamed because it was a Python reserved word.
#     generic = models.CharField(max_length=30, blank=True, null=True)
#     type = models.CharField(max_length=30, blank=True, null=True)
#     origin = models.CharField(max_length=30, blank=True, null=True)
#     country = models.CharField(max_length=30, blank=True, null=True)
#     trait = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'tree_species'
#
#
# class TreeUser(models.Model):
#     entity_id = models.IntegerField()
#     pno = models.IntegerField()
#     pname = models.CharField(max_length=20)
#     p_x = models.FloatField()
#     p_y = models.FloatField()
#     longitude = models.FloatField(blank=True, null=True)
#     latitude = models.FloatField(blank=True, null=True)
#     altitude = models.FloatField(blank=True, null=True)
#     height = models.FloatField(blank=True, null=True)
#     dbh = models.FloatField(blank=True, null=True)
#     region_id = models.IntegerField(blank=True, null=True)
#     plant_company = models.CharField(max_length=50, blank=True, null=True)
#     plant_date = models.DateField(blank=True, null=True)
#     place = models.CharField(max_length=50, blank=True, null=True)
#     rate = models.CharField(max_length=50, blank=True, null=True)
#     feature = models.CharField(max_length=50, blank=True, null=True)
#     usage = models.CharField(max_length=50, blank=True, null=True)
#     health = models.CharField(max_length=50, blank=True, null=True)
#     introduction = models.TextField(blank=True, null=True)
#     gender = models.CharField(max_length=4, blank=True, null=True)
#     age = models.IntegerField(blank=True, null=True)
#     image_id = models.IntegerField(blank=True, null=True)
#     recorder_id = models.IntegerField()
#     create_date = models.DateTimeField(blank=True, null=True)
#     way = models.IntegerField(blank=True, null=True)
#     checked = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tree_user'
#
#
# class User(models.Model):
#     uid = models.IntegerField(primary_key=True)
#     uname = models.CharField(max_length=30, blank=True, null=True)
#     passport = models.CharField(max_length=20, blank=True, null=True)
#     upriority = models.IntegerField(blank=True, null=True)
#     ucompany = models.CharField(max_length=30, blank=True, null=True)
#     regist_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user'


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Code(models.Model):
    cid = models.IntegerField(primary_key=True)
    cno = models.IntegerField(blank=True, null=True)
    cname = models.CharField(max_length=20, blank=True, null=True)
    des = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'code'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Edit(models.Model):
    inforwindow = models.CharField(max_length=30, blank=True, null=True)
    background = models.CharField(max_length=30, blank=True, null=True)
    addition = models.CharField(max_length=30, blank=True, null=True)
    details = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'edit'


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
    class_field = models.CharField(db_column='class', max_length=30, blank=True,
                                   null=True)  # Field renamed because it was a Python reserved word.
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
