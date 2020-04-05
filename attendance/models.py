from enum import Enum
from django.db import models
from django_enumfield import enum
from django_enum_choices.fields import EnumChoiceField
from django.contrib.auth.models import User

from booking.models import Booking
from staff.models import Staff


class Attendance(models.Model):
    type = models.CharField(max_length=100)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, null=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True)
    in_time = models.DateTimeField()
    gate_no = models.CharField(max_length=100)
    person_quantity = models.IntegerField()
    out_time = models.DateTimeField(null=True)
    out_gate_no = models.CharField(max_length=100, null=True)
    vehicle = models.CharField(max_length=20, null=True)
    vehicle_quantity = models.IntegerField(null=True)
    note = models.CharField(max_length=250, null=True)
    authorized_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
