import datetime

from django.contrib.auth.models import User
from django.db import transaction
from rest_framework.utils import json
from rest_framework.views import APIView

from account.models import Account
from booking.models import Booking
from duty.models import Duty
from guard.models import Guard
from htech.globalMethods import GetListData, GetSerializeData, hasRoleId, hasRole
from django.http import JsonResponse

from htech.serializers import UserSerializer, RoleUserSerializer, PermissionSerializer
from permission.models import Permission
from role.models import Role
from roleUser.models import RoleUser


def index(request):
    user = GetListData()
    data = user.get(request, RoleUser.objects.all(), RoleUserSerializer, 'User')

    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def create(request):
    roles = Role.objects.all()
    return JsonResponse({
        'roles': list(roles.values()),
    })


def store(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        with transaction.atomic():
            user_name = data['user']['username'].replace(" ", "")
            new_user = User.objects.create_user(username=user_name.lower(),
                                                email=data['user']['email'],
                                                password=data['user']['password'],
                                                first_name=data['user']['first_name'],
                                                last_name=data['user']['last_name'],
                                                is_active=data['user']['status'] == 'Active' if 1 else 0
                                                )
            RoleUser.objects.create(
                role_id=data['user']['role']['id'],
                user_id=new_user.id
            )
            return JsonResponse({'type': 'success', 'message': 'User Created Successfully'})


def edit(request, id):
    user = GetUser()
    user = user.get(id)[0]
    roles = Role.objects.all()
    return JsonResponse({
        'user': user,
        'roles': list(roles.values()),
    })


class GetUser(APIView):

    def get(self, id):
        query = RoleUser.objects.filter(user_id__exact=id)
        serializers = RoleUserSerializer(query, many=True)
        return serializers.data


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        with transaction.atomic():
            user_name = data['user']['username'].replace(" ", "")
            user = User.objects.filter(id=id)
            user.update(
                username=user_name.lower(),
                email=data['user']['email'],
                first_name=data['user']['first_name'],
                last_name=data['user']['last_name'],
                is_active=data['user']['status'] == 'Active' if 1 else 0
            )
            if data['user']['password']:
                user.set_password(data['user']['password'])
                user.save()

            return JsonResponse({'type': 'success', 'message': 'Staff Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        with transaction.atomic():
            User.objects.filter(id=id).delete()
            RoleUser.objects.filter(user_id=id).delete()
            return JsonResponse({'type': 'success', 'message': 'User Deleted Successfully'})


def get_user(request):
    query = User.objects.filter(id=request.user.id)
    serialize_data = GetSerializeData()
    user_data = serialize_data.get(query, UserSerializer)
    other_data = None
    guard_data = []
    guard_duty = None

    if request.user.is_superuser:
        permissions = 'Admin'
        role_data = 'Admin'
        other_data = Account.objects.filter(user_id=1)
    else:
        permissions = serialize_data.get(Permission.objects.filter(role_id=hasRoleId(request)), PermissionSerializer)
        role_data = {'name': hasRole(request), 'id': hasRoleId(request)}

    if other_data:
        other_data = list(other_data.values())
    else:
        other_data = 'Sorry'

    if hasRole(request) == 'Guard':
        guard = Guard.objects.filter(user_id=request.user.id).first()
        guard_data = Duty.objects.filter(guard_id=guard.id).order_by('-id').values()
        guard_duty = Duty.objects.filter(guard_id=guard.id,
                                         from_time__lte=datetime.datetime.now() - datetime.timedelta(minutes=5),
                                         to_time__gte=datetime.datetime.now()).count()
    return JsonResponse({
        'user': user_data[0],
        'permission': permissions,
        'role_data': role_data,
        'other_data': other_data,
        'guard_data': list(guard_data),
        'guard_duty': guard_duty
    })


def change_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if request.user.check_password(data['existing_password']):
            request.user.set_password(data['new_password'])
            request.user.save()
            return JsonResponse(
                {'type': 'success', 'message': "Password Updated Successfully"})
        else:
            return JsonResponse(
                {'type': 'error', 'message': "Existing Password didn't match if you forgot the contact with admin"})


def change_details(request):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        user = User.objects.filter(id=request.user.id)
        if user:
            user.update(
                first_name=data['user']['first_name'],
                last_name=data['user']['last_name'],
                email=data['user']['email'],
                is_active=data['user']['status'] == 'Active' if 1 else 0,
            )

            return JsonResponse(
                {'type': 'success', 'message': "User info Updated Successfully"})
