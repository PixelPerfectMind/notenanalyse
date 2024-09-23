from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

class Subject(models.Model):
    id = models.Index
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    updated_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(datetime.now())

class Symbol(models.Model):
    id = models.Index
    content = models.CharField(max_length=16)

class SchoolYear(models.Model):
    id = models.Index
    name = models.CharField(max_length=64)
    starts_at = models.DateTimeField()
    ends_at = models.DateTimeField(blank=True, null=True)

class User_Subject(models.Model):
    id = models.Index
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    symbol_id = models.ForeignKey(Symbol, on_delete=models.DO_NOTHING)
    school_year_id = models.ForeignKey(SchoolYear, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(datetime.now())
    updated_at = models.DateTimeField(blank=True, null=True)