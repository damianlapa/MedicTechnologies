from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group


class UserToken(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    token = models.CharField(max_length=16, unique=True)
    password_reset = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now=True)


class Technology(models.Model):
    name = models.CharField(max_length=64, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)


class Analysts(Group):
    name = 'Analysts'
