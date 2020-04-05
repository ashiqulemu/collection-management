from enum import Enum
from django.db import models
from django_enumfield import enum
from django_enum_choices.fields import EnumChoiceField

from company.models import Company


class Staff(models.Model):
    staff_id = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    mobile = models.CharField(max_length=20, null=True)
    rf_id = models.CharField(max_length=50, null=True)
    profile_image = models.TextField(max_length=250, null=True)
    finger_print = models.CharField(max_length=250, null=True)
    status = models.CharField(max_length=250)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()

#Designation Need to be implement
