from enum import Enum
from django.contrib.auth.models import User
from django.db import models
from django_enumfield import enum
from django_enum_choices.fields import EnumChoiceField
from building.models import Building


class Company(models.Model):
    name = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    authorize_person = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, default=0)
    mobile = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=30, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()


# Active/Inactive Implementation