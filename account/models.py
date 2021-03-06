from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.CharField(max_length=255, null=True)
