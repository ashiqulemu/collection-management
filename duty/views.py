from django.db import transaction
from django.db.models import Count
from rest_framework.views import APIView
from duty.models import Duty
from guard.models import Guard
from htech.globalMethods import GetListData, get_date_time, hasRole
import json
from django.http import JsonResponse
import datetime

from htech.serializers import DutySerializer


def index(request):
    duty = GetListData()
    if hasRole(request) == 'Guard':
        guard_id = Guard.objects.filter(user_id=request.user.id).first().id
        data = duty.get(request, Duty.objects.filter(guard_id=guard_id), DutySerializer, 'Duty')

    else:
        data = duty.get(request, Duty.objects.all(), DutySerializer, 'Duty')
    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def create(request):
    guards = Guard.objects.filter(status__exact='Active')
    return JsonResponse({
        'guards': list(guards.values()),
    })


def store(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        Duty.objects.create(
            guard_id=data['duty']['guard']['id'],
            gate_no=data['duty']['gate_no'],
            from_time=get_date_time(data['duty']['from_time']),
            to_time=get_date_time(data['duty']['to_time']),
            update_at=datetime.datetime.now(),
            created_at=datetime.datetime.now()
        )
        return JsonResponse({'type': 'success', 'message': 'Duty Created Successfully'})


def multi_store(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        with transaction.atomic():
            for item in data['dutyItem']:
                Duty.objects.create(
                    guard_id=data['duty']['guard']['id'],
                    gate_no=item['gate'],
                    from_time=item['from_time'],
                    to_time=item['to_time'],
                    update_at=datetime.datetime.now(),
                    created_at=datetime.datetime.now()
                )
            return JsonResponse({'type': 'success', 'message': 'Duty Created Successfully'})


def edit(request, id):
    duty = GetDuty()
    duty = duty.get(id)[0]
    guards = Guard.objects.filter(status__exact='Active')
    return JsonResponse({
        'duty': duty,
        'guards': list(guards.values()),
    })


class GetDuty(APIView):

    def get(self, id):
        query = Duty.objects.filter(id=id)
        serializers = DutySerializer(query, many=True)
        return serializers.data


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        Duty.objects.filter(id=id).update(
            guard_id=data['duty']['guard']['id'],
            gate_no=data['duty']['gate_no'],
            from_time=get_date_time(data['duty']['from_time']),
            to_time=get_date_time(data['duty']['to_time']),
            update_at=datetime.datetime.now()
        )
        return JsonResponse({'type': 'success', 'message': 'Duty Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        Duty.objects.filter(id=id).delete()
        return JsonResponse({'type': 'success', 'message': 'Duty Deleted Successfully'})
