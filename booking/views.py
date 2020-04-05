from django.db.models import CharField, Value
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

from booking.models import Booking
from company.models import Company
from htech.globalMethods import GetListData, hasRole, get_company_by_user, get_date_time
import json
from django.http import JsonResponse
import datetime
from django.utils import timezone

from htech.serializers import BookingSerializer


def index(request):
    booking = GetListData()
    if hasRole(request) == 'Company':
        company_id = get_company_by_user(request).id
        data = booking.get(request, Booking.objects.filter(
            company_id__exact=company_id), BookingSerializer, 'Booking')
    else:
        data = booking.get(request, Booking.objects.all(), BookingSerializer, 'Booking')

    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def create(request):
    if hasRole(request) == 'Company':
        company_id = get_company_by_user(request).id
        companies = Company.objects.filter(status__exact='Active', id=company_id)[:4]
    else:
        companies = Company.objects.filter(status__exact='Active')[:4]
    return JsonResponse({
        'companies': list(companies.values()),
    })


def store(request, user_id=None):
    if request.method == 'POST':
        data = json.loads(request.body)
        Booking.objects.create(
            name=data['booking']['name'],
            company_id=data['booking']['company']['id'],
            user_id=user_id if user_id else request.user.id,
            mobile=data['booking']['mobile'],
            guest_quantity=data['booking']['guest_quantity'],
            date_time=data['booking']['date_time'],
            note=data['booking']['note'],
            update_at=datetime.datetime.now(),
            created_at=datetime.datetime.now()
        )
    return JsonResponse({'type': 'success', 'message': 'Booking Created Successfully'})


def edit(request, id):
    booking = GetAttendance()
    booking = booking.get(id)[0]
    if hasRole(request) == 'Company':
        company_id = get_company_by_user(request).id
        companies = Company.objects.filter(status__exact='Active', id=company_id)
    else:
        booked = Booking.objects.filter(id=id).first()
        companies = Company.objects.filter(status__exact='Active', id=booked.company_id)
    return JsonResponse({
        'booking': booking,
        'companies': list(companies.values()),
    })


class GetAttendance(APIView):

    def get(self, id):
        query = Booking.objects.filter(id=id)
        serializers = BookingSerializer(query, many=True)
        return serializers.data


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        Booking.objects.filter(id=id).update(
            name=data['booking']['name'],
            company_id=data['booking']['company']['id'],
            mobile=data['booking']['mobile'],
            guest_quantity=data['booking']['guest_quantity'],
            date_time=data['booking']['date_time'],
            note=data['booking']['note'],
            update_at=datetime.datetime.now(),
        )
        return JsonResponse({'type': 'success', 'message': 'Booking Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        Booking.objects.filter(id=id).delete()
        return JsonResponse({'type': 'success', 'message': 'Booking Deleted Successfully'})


def get_booking(request, id):
    booking = Booking.objects.filter(id=id).annotate(model_type=Value('booking', output_field=CharField()))
    return JsonResponse({
        'booking': list(booking.values('id', 'name', 'guest_quantity', 'model_type'))[0],
    })
