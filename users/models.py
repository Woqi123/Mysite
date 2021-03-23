# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    mobile_phone = models.CharField(max_length=255, blank=True, null=True)
    tel_phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    crt_time = models.DateTimeField(blank=True, null=True)
    crt_user = models.CharField(max_length=255, blank=True, null=True)
    crt_name = models.CharField(max_length=255, blank=True, null=True)
    crt_host = models.CharField(max_length=255, blank=True, null=True)
    upd_time = models.DateTimeField(blank=True, null=True)
    upd_user = models.CharField(max_length=255, blank=True, null=True)
    upd_name = models.CharField(max_length=255, blank=True, null=True)
    upd_host = models.CharField(max_length=255, blank=True, null=True)
    attr1 = models.CharField(max_length=255, blank=True, null=True)
    attr2 = models.CharField(max_length=255, blank=True, null=True)
    attr3 = models.CharField(max_length=255, blank=True, null=True)
    attr4 = models.CharField(max_length=255, blank=True, null=True)
    attr5 = models.CharField(max_length=255, blank=True, null=True)
    attr6 = models.CharField(max_length=255, blank=True, null=True)
    attr7 = models.CharField(max_length=255, blank=True, null=True)
    attr8 = models.CharField(max_length=255, blank=True, null=True)
