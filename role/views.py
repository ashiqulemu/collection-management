from django.core.exceptions import ValidationError
from django.db import transaction
from rest_framework.views import APIView

from htech.globalMethods import GetListData
from htech.serializers import RoleSerializer
from permission.models import Permission
from roleUser.models import RoleUser
from .models import Role
import json
from django.http import JsonResponse


def index(request):
    role = GetListData()
    data = role.get(request, Role.objects.all(), RoleSerializer, 'Role')
    return JsonResponse({
        'data': data[0],
        'pagination': data[1],
    })


def create(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        if Role.objects.filter(name=data['role']['name']).exists():
            return JsonResponse({'type': 'error', 'message': 'Role Name Already Exist'})
        else:
            with transaction.atomic():
                role = Role.objects.create(name=data['role']['name'])
                permission_create(role.id)
                return JsonResponse({'type': 'success', 'message': 'Role Created Successfully'})


def edit(request, id):
    role = Role.objects.filter(id=id).values()
    return JsonResponse({'result': list(role)[0]})


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        with transaction.atomic():
            Role.objects.filter(id=id).update(name=data['role']['name'])
            return JsonResponse({'type': 'success', 'message': 'Role Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        with transaction.atomic():

            if RoleUser.objects.filter(role_id=id).count():
                return JsonResponse(
                    {'type': 'error', 'message': 'Role already assign with user, Please delete user first'})
            else:
                Role.objects.filter(id=id).delete()
                return JsonResponse({'type': 'success', 'message': 'Role Deleted Successfully'})


def permission_create(role_id):
    moduled_data = ['Company', 'Booking', 'Attendance', 'Staff', 'Guard', 'Duty', 'User', 'Role-Permission',
                    'Duty-History', 'Building']
    with transaction.atomic():
        for item in moduled_data:
            Permission.objects.create(
                moduled=item,
                role_id=role_id,
            )


def get_role(request):
    roles = GetRole()
    roles = roles.get()
    return JsonResponse({'roles': list(roles)})


class GetRole(APIView):

    def get(self):
        query = Role.objects.all()
        serializers = RoleSerializer(query, many=True)
        return serializers.data
