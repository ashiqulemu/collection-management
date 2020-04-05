from django.db import transaction
from django.db.models import CharField, Value
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

from building.models import Building
from company.models import Company
from htech.globalMethods import GetListData, hasRole, get_company_by_user, get_date_time
import json
from django.http import JsonResponse
import datetime
from django.utils import timezone

from htech.serializers import BuildingSerializer


def index(request):
    building = GetListData()
    data = building.get(request, Building.objects.all(), BuildingSerializer, 'Building')

    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def store(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Building.objects.create(
                name=data['building']['name'],
        )
        return JsonResponse({'type': 'success', 'message': 'Building Created Successfully'})


def edit(request, id):
    building = Building.objects.filter(id=id).values()
    return JsonResponse({'result': list(building)[0]})


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        with transaction.atomic():
            building = Building.objects.filter(id=id)
            building.update(
                name=data['building']['name'],
            )

            return JsonResponse({'type': 'success', 'message': 'Building Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        if Company.objects.filter(building_id=id).count() > 0:
            return JsonResponse({'type': 'error', 'message': 'Building associate with Company'})
        else:
            Building.objects.filter(id=id).delete()
            return JsonResponse({'type': 'success', 'message': 'Building Deleted Successfully'})

