from django.contrib.auth.models import User
from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponse

from role.views import permission_create
from roleUser.models import RoleUser
from guard.models import Guard
from htech.globalMethods import GetListData
import json
from django.http import JsonResponse
import datetime
from django.utils import timezone

from htech.serializers import GuardSerializer
from role.models import Role


def index(request):
    guard = GetListData()
    data = guard.get(request, Guard.objects.all(), GuardSerializer, 'Guard')

    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        with transaction.atomic():
            user_name = data['guard']['guard_id'].replace(" ", "")
            new_user = User.objects.create_user(username=user_name.lower(),
                                                password=123456,
                                                first_name=data['guard']['first_name'],
                                                last_name=data['guard']['last_name'],
                                                is_active=data['guard']['status'] == 'Active' if 1 else 0
                                                )
            Guard.objects.create(
                guard_id=data['guard']['guard_id'],
                name=data['guard']['first_name']+' '+data['guard']['last_name'],
                nid=data['guard']['nid'],
                mobile=data['guard']['mobile'],
                rf_id=data['guard']['rf_id'],
                status=data['guard']['status'],
                user_id=new_user.id,
                update_at=datetime.datetime.now(),
                created_at=datetime.datetime.now()
            )
            role_user = Role.objects.filter(name__icontains='Guard')
            if role_user:
                RoleUser.objects.create(
                    role_id=role_user.first().id,
                    user_id=new_user.id
                )
            else:
                new_role = Role.objects.create(name='Guard')
                permission_create(new_role.id)
                RoleUser.objects.create(
                    role_id=new_role.id,
                    user_id=new_user.id
                )
            return JsonResponse({'type': 'success', 'message': 'Guard Created Successfully'})


def edit(request, id):
    guard = Guard.objects.filter(id=id).values()
    return JsonResponse({'result': list(guard)[0]})


def update(request, id):
    if request.method == 'PATCH':
        with transaction.atomic():
            data = json.loads(request.body)
            guard = Guard.objects.filter(id=id)
            guard.update(
                guard_id=data['guard']['guard_id'],
                name=data['guard']['name'],
                nid=data['guard']['nid'],
                mobile=data['guard']['mobile'],
                rf_id=data['guard']['rf_id'],
                status=data['guard']['status'],
                update_at=datetime.datetime.now(),
            )
            User.objects.filter(id=guard.first().user_id).update(
                username=data['guard']['guard_id'].replace(" ", "").lower(),
                is_active=data['guard']['status'] == 'Active' if 1 else 0
            )

            return JsonResponse({'type': 'success', 'message': 'Guard Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        guard = Guard.objects.filter(id=id)
        if guard.first().user_id:
            User.objects.filter(id=guard.first().user_id).delete()

        guard.delete()
        return JsonResponse({'type': 'success', 'message': 'Guard Deleted Successfully'})
