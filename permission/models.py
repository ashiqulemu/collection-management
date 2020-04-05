from django.db import models
from django.contrib.auth.models import User

from role.models import Role


class Permission(models.Model):
    moduled = models.CharField(max_length=200)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='role_user')
    create_permission = models.BooleanField(default=False)
    edit_permission = models.BooleanField(default=False)
    view_permission = models.BooleanField(default=False)
    delete_permission = models.BooleanField(default=False)
    share_permission = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
