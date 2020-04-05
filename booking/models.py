from django.contrib.auth.models import User
from django.db import models

from company.models import Company


class Booking(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    mobile = models.CharField(max_length=30, null=True)
    guest_quantity = models.IntegerField()
    date_time = models.DateTimeField()
    note = models.CharField(max_length=100, null=True)
    is_attendance = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
