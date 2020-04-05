from django.contrib.auth.models import User
from django.db import models


class Guard(models.Model):
    guard_id = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20, null=True)
    profile_image = models.CharField(max_length=100,null=True)
    rf_id = models.CharField(max_length=20)
    status = models.CharField(max_length=250)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    update_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)


