from django.db import transaction
from django.db.models import Value, CharField, Q
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from attendance.models import Attendance
from booking.models import Booking
from htech.globalMethods import GetListData, hasRole, get_company_by_user, get_date_time
import json
from django.http import JsonResponse
import datetime
from django.utils import timezone

from htech.serializers import AttendanceSerializer
from staff.models import Staff


def index(request):
    attendance = GetListData()
    if hasRole(request) == 'Company':
        company_id = get_company_by_user(request).id
        data = attendance.get(request, Attendance.objects.filter(
            Q(staff__company__id=company_id) | Q(booking__company__id=company_id)), AttendanceSerializer, 'Attendance')
    else:
        data = attendance.get(request, Attendance.objects.all(), AttendanceSerializer, 'Attendance')

    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def create(request):
    booking = Booking.objects.filter(is_attendance__exact=0).annotate(
        model_type=Value('booking', output_field=CharField()))
    staffs = Staff.objects.filter(status__exact='Active').annotate(model_type=Value('staff', output_field=CharField()))
    return JsonResponse({
        'staffs': list(staffs.union(booking).values('id', 'name', 'model_type', 'company__name')),
    })


def store(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        staff_id = None
        booking_id = None
        if data['attendance']['type'] == 'Staff':
            staff_id = data['attendance']['staff']['id']

        if data['attendance']['type'] == 'Visitor':
            booking_id = data['attendance']['staff']['id']
        attendance = Attendance.objects.create(
            type=data['attendance']['type'],
            staff_id=staff_id,
            booking_id=booking_id,
            in_time=get_date_time(data['attendance']['in_time']),
            person_quantity=data['attendance']['person_quantity'],
            out_time=get_date_time(data['attendance']['out_time']),
            gate_no=data['attendance']['gate_no'],
            out_gate_no=data['attendance']['out_gate_no'],
            vehicle=data['attendance']['vehicle'],
            vehicle_quantity=data['attendance']['vehicle_quantity'],
            note=data['attendance']['note'],
            authorized_by=request.user,
            update_at=datetime.datetime.now(),
            created_at=datetime.datetime.now()
        )

        if attendance and data['attendance']['booking_id']:
            Booking.objects.filter(id=data['attendance']['booking_id']).update(is_attendance=True)

        return JsonResponse({'type': 'success', 'message': 'Entry Created Successfully'})


def edit(request, id):
    attendance = GetAttendance()
    attendance = attendance.get(id)[0]
    booking = Booking.objects.annotate(
        model_type=Value('booking', output_field=CharField()))
    staffs = Staff.objects.filter(status__exact='Active').annotate(model_type=Value('staff', output_field=CharField()))

    return JsonResponse({
        'attendance': attendance,
        'staffs': list(staffs.union(booking).values('id', 'name', 'model_type', 'company__name')),
    })


class GetAttendance(APIView):

    def get(self, id):
        query = Attendance.objects.filter(id=id)
        serializers = AttendanceSerializer(query, many=True)
        return serializers.data


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        staff_id = None
        booking_id = None
        if data['attendance']['type'] == 'Staff':
            staff_id = data['attendance']['staff']['id']

        if data['attendance']['type'] == 'Visitor':
            booking_id = data['attendance']['staff']['id']

        Attendance.objects.filter(id=id).update(
            type=data['attendance']['type'],
            staff_id=staff_id,
            booking_id=booking_id,
            in_time=get_date_time(data['attendance']['in_time']),
            out_time=get_date_time(data['attendance']['out_time']),
            gate_no=data['attendance']['gate_no'],
            out_gate_no=data['attendance']['out_gate_no'],
            vehicle=data['attendance']['vehicle'],
            note=data['attendance']['note'],
            update_at=datetime.datetime.now(),
        )
        return JsonResponse({'type': 'success', 'message': 'Attendance Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        Attendance.objects.filter(id=id).delete()
        return JsonResponse({'type': 'success', 'message': 'Attendance Deleted Successfully'})
