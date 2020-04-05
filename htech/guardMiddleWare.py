import datetime

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout

from duty.models import Duty
from guard.models import Guard
from htech.globalMethods import hasRole


class GuardActivities:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        path = request.get_full_path()

        # if hasRole(request) == 'Guard':
            # if not check_guard_schedule(request):
                # messages.add_message(request, messages.INFO,
                #                      'Your duty is not in this slot. Please Contact with your supervisor.')
                # django_logout(request)
                # response = redirect('/accounts/login/')
                # return response

        return response


def check_guard_schedule(request):
    guard = Guard.objects.filter(user_id=request.user.id).first()
    duty = Duty.objects.filter(guard_id=guard.id, from_time__lte=datetime.datetime.now()-datetime.timedelta(minutes=5),
                               to_time__gte=datetime.datetime.now())
    if duty.count():
        return True
    else:
        return False
