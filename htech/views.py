from django.http import JsonResponse
from django.contrib.auth import login as django_login, logout as django_logout
from zk import ZK, const
import datetime

from dutyHistory.models import DutyHistory
from guard.models import Guard
from htech.globalMethods import hasRole


def logout(request):
    if request.method == "POST":
        if hasRole(request) == 'Guard':
            guard = Guard.objects.filter(user_id=request.user.id).first()
            duty = DutyHistory.objects.filter(guard_id__exact=guard.id).order_by('-id').first()
            if duty:
                DutyHistory.objects.filter(id=duty.id).update(
                    logout_time=datetime.datetime.now(),
                    update_at=datetime.datetime.now(),
                )
            django_logout(request)

        else:
            django_logout(request)

        return JsonResponse({'result': 'success', })


def finger(request):
    conn = None
    # create ZK instance
    zk = ZK('192.168.3.207', port=4370, timeout=5)
    try:
        conn = zk.connect()
        conn.disable_device()

        conn.test_voice()
        newtime = datetime.datetime.today()
        conn.set_time(newtime)
        conn.enable_device()
    except Exception as e:
        print("Process terminate : {}".format(e))
    finally:
        if conn:
            # for attendance in conn.live_capture():
            #     if attendance is None:
            #         # implement here timeout logic
            #         pass
            #     else:
            #         print(attendance)  # Attendance object
            # # conn.set_user(uid=5, name='Sorif Uddin', privilege=const.USER_ADMIN, password='12345678', group_id='',
            # #               user_id='126', card=0)
            # attendances = len(conn.get_attendance())
            # print(attendances)
            # print(conn.get_user_template(uid=5, temp_id=6))

            conn.disconnect()

    return JsonResponse({'result': 'Finger Print Device Connected an Done Activities', })

# 1) Problem to set fingerprint to store when user create from our software()
# 2) Get attendance return all attendance result so it will be return huge data at the end
# 3) Live attendance system has but need set a corn job
