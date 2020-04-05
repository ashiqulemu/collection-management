from django.db import models
from django.contrib.auth.models import User

from role.models import Role


class RoleUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
