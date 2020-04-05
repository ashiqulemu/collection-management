from django.db import models

from guard.models import Guard


class Duty(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE, null=True)
    gate_no = models.CharField(max_length=100)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()
