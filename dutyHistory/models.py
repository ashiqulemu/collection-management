import datetime

from django.db import models

from duty.models import Duty
from htech.globalMethods import hasRole
from htech.guardMiddleWare import check_guard_schedule
from guard.models import Guard
import logging
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


class DutyHistory(models.Model):
    guard = models.ForeignKey(Guard, on_delete=models.CASCADE, null=True)
    gate_no = models.CharField(max_length=100)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField(null=True)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    if hasRole(request) == 'Guard':
        if check_guard_schedule(request):
            guard = Guard.objects.filter(user_id=request.user.id).first()
            duty = Duty.objects.filter(guard_id=guard.id, from_time__lte=datetime.datetime.now(),
                                       to_time__gte=datetime.datetime.now())

            DutyHistory.objects.create(
                guard_id=guard.id,
                gate_no=duty.first().gate_no,
                login_time=datetime.datetime.now(),
                logout_time=None,
                update_at=datetime.datetime.now(),
                created_at=datetime.datetime.now()
            )


