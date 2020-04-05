from django.contrib.auth.models import User
from rest_framework.utils import json

from htech.globalMethods import GetListData, GetSerializeData
from django.http import JsonResponse

from htech.serializers import RoleUserSerializer
from roleUser.models import RoleUser


def index(request):
    role_user = GetListData()
    data = role_user.get(request, RoleUser.objects.all(), RoleUserSerializer, 'RoleUser')

    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def assign(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        role_user = RoleUser.objects.filter(user_id__exact=data['user']['id'])
        if role_user.count():
            role_user.update(
                role_id=data['role']['id'],
                user_id=data['user']['id']
            )
        else:
            RoleUser.objects.create(
                role_id=data['role']['id'],
                user_id=data['user']['id']
            )
        return JsonResponse({'type': 'success', 'message': 'Staff Created Successfully'})
