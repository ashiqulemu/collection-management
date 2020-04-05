from rest_framework.views import APIView
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
import datetime
from rest_framework.authtoken.models import Token
from company.models import Company
from htech import settings
from role.models import Role
from roleUser.models import RoleUser


class GetSerializeData(APIView):

    def get(self, data, serilize_name):
        serializers = serilize_name(data, many=True)
        return serializers.data


def hasRole(request):
    if RoleUser.objects.filter(user_id=request.user.id):
        roleData = RoleUser.objects.filter(user_id=request.user.id)
        return list(roleData.values('role__name'))[0]['role__name']
    else:
        if request.user.is_superuser:
            return 'Admin'


def hasRoleId(request):
    if RoleUser.objects.filter(user_id=request.user.id):
        roleData = RoleUser.objects.filter(user_id=request.user.id)
        return list(roleData.values('role__id'))[0]['role__id']
    else:
        if request.user.is_superuser:
            return 'Admin'


def getUserByToken(request):
    access_token = request.META.get('HTTP_AUTHORIZATION', '')
    if access_token:
        access_token = access_token.replace("Bearer ", "")
        user = Token.objects.get(key=access_token).user
        return user
    else:
        return None


def get_date_time(data):
    if data:
        date = data[0:10]
        time = data[11:19]
        data = date + ' ' + time
        return datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=settings.DELTA_HOURS)
    else:
        return None


def get_company_by_user(request):
    return Company.objects.filter(user_id=request.user.id).first()


class GetListData(APIView):

    def get(self, request, query, serialize, type=None):
        v = request.GET.get('searchValue')

        if type == 'Company':
            query = company_search(v, request, query)
        elif type == 'Staff':
            query = staff_search(v, request, query)
        elif type == 'Attendance':
            query = attendance_search(v, request, query)
        elif type == 'Duty':
            query = duty_search(v, request, query)
        elif type == 'User':
            query = user_search(v, request, query)
        elif type == 'DutyHistory':
            query = duty_history_search(v, request, query)
        elif type == 'Booking':
            if request.GET.get('queue'):
                query = query.filter(is_attendance__exact=0)
            query = booking_search(v, request, query)
        else:
            query = common_search(v, request, query)

        if request.GET.get('sortOrder') == 'DESC':
            query = query.order_by('-' + request.GET.get('sortBy') if request.GET.get('sortBy') else 'id')
        else:
            query = query.order_by(request.GET.get('sortBy'))

        if request.GET.get('rowsPerPage'):
            p = Paginator(query, request.GET.get('rowsPerPage'))

        page1 = p.page(request.GET.get('page'))

        serializers = serialize(page1, many=True)

        return [serializers.data, p.count]


def company_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(name__icontains=v) | Q(owner__icontains=v)
                             | Q(mobile__icontains=v) | Q(building__name__icontains=v) | Q(email__icontains=v))

    return query


def staff_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(name__icontains=v) | Q(staff_id__icontains=v)
                             | Q(mobile__icontains=v) | Q(rf_id__icontains=v) | Q(company__name__icontains=v))

    if request.GET.get('company'):
        query = query.filter(Q(company_id__exact=request.GET.get('company')))
    return query


def attendance_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(type__icontains=v)
                             | Q(booking__name__icontains=v)
                             | Q(gate_no__icontains=v) | Q(out_gate_no__icontains=v) | Q(vehicle__icontains=v))
    if request.GET.get('date'):
        query = query.filter(Q(in_time__icontains=request.GET.get('date')))

    return query


def booking_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(name__icontains=v) | Q(company__name__icontains=v)
                             | Q(mobile__icontains=v) | Q(guest_quantity__icontains=v))
    if request.GET.get('date'):
        query = query.filter(Q(date_time__icontains=request.GET.get('date')))

    return query


def duty_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(gate_no__icontains=v) | Q(guard__name__icontains=v))

    if request.GET.get('date'):
        query = query.filter(Q(from_time__icontains=request.GET.get('date')))

    return query


def duty_history_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(gate_no__icontains=v) | Q(guard__name__icontains=v)
                             | Q(login_time__icontains=v) | Q(logout_time__icontains=v))

    return query


def user_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(user__username__icontains=v) | Q(role__name__icontains=v)
                             | Q(user__email__icontains=v))

    return query


def common_search(v, request, query):
    if request.GET.get('searchValue'):
        query = query.filter(Q(name__icontains=v))
    return query
