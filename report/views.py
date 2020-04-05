from attendance.models import Attendance
from django.http import JsonResponse
import datetime
from company.models import Company
from duty.models import Duty
from guard.models import Guard
from htech.globalMethods import get_company_by_user
from staff.models import Staff
from django.utils import timezone


def dashboard_report(request):
    visitor_today = 0
    total_company = 0
    security_guard = 0
    total_staff = 0
    if request.GET.get('type') == 'dashboard':
        visitor_today = Attendance.objects.filter(created_at__icontains=datetime.date.today(),
                                                  type__exact='Visitor').count()
        total_company = Company.objects.filter(status__exact='Active').count()
        security_guard = Guard.objects.filter(status__exact='Active').count()
        total_staff = Staff.objects.filter(status__exact='Active', company__status__exact='Active').count()
    if request.GET.get('type') == 'company':
        com_id = get_company_by_user(request).id
        visitor_today = Attendance.objects.filter(created_at__icontains=datetime.date.today(),
                                                  staff__company_id=com_id,
                                                  booking__company_id=com_id,
                                                  type__exact='Visitor').count()
        total_staff = Staff.objects.filter(status__exact='Active', company__status__exact='Active',
                                           company_id__exact=com_id).count()
    if request.GET.get('type') == 'guard':
        visitor_today = Attendance.objects.filter(created_at__icontains=datetime.date.today(),
                                                  type__exact='Visitor').count()
        total_company = Company.objects.filter(status__exact='Active').count()
        total_staff = Staff.objects.filter(status__exact='Active', company__status__exact='Active').count()

    return JsonResponse({
        'visitor_today': visitor_today,
        'total_company': total_company,
        'security_guard': security_guard,
        'total_staff': total_staff,
    })
