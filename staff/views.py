import os
import uuid
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.db import transaction
from django.db.models import Q
from rest_framework.views import APIView
from company.models import Company
from staff.models import Staff
from htech.globalMethods import GetListData, hasRole, get_company_by_user
from django.http import JsonResponse
import datetime
from htech.serializers import StaffSerializer
from django.conf import settings
from htech import settings as setting


def index(request):
    staff = GetListData()
    if hasRole(request) == 'Company':
        company_id = get_company_by_user(request).id
        data = staff.get(request, Staff.objects.filter(
            Q(company_id=company_id)), StaffSerializer, 'Staff')
    else:
        data = staff.get(request, Staff.objects.all(), StaffSerializer, 'Staff')

    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def create(request):
    if hasRole(request) == 'Company':
        company_id = get_company_by_user(request).id
        companies = Company.objects.filter(status__exact='Active', id=company_id)
    else:
        companies = Company.objects.filter(status__exact='Active')
    return JsonResponse({
        'companies': list(companies.values()),
    })


def store(request):
    if request.method == 'POST':
        data = request.POST
        img_url = get_image_url(request, 'staff')
        with transaction.atomic():
            Staff.objects.create(
                staff_id=data['staff_id'],
                name=data['name'],
                mobile=data['mobile'],
                rf_id=data['rf_id'],
                company_id=data['company'],
                status=data['status'],
                profile_image=img_url,
                update_at=datetime.datetime.now(),
                created_at=datetime.datetime.now()
            )
            return JsonResponse({'type': 'success', 'message': 'Staff Created Successfully'})


def edit(request, id):
    staff = GetStaff()
    staff = staff.get(id)[0]
    if hasRole(request) == 'Company':
        company_id = get_company_by_user(request).id
        companies = Company.objects.filter(status__exact='Active', id=company_id)
    else:
        companies = Company.objects.filter(status__exact='Active')
    return JsonResponse({
        'staff': staff,
        'companies': list(companies.values()),
    })


class GetStaff(APIView):

    def get(self, id):
        query = Staff.objects.filter(id=id)
        serializers = StaffSerializer(query, many=True)
        return serializers.data


def update(request, id):
    if request.method == 'POST':
        data = request.POST
        img_url = get_image_url(request, 'staff', 'update', Staff.objects.filter(id=id).get())
        print(datetime.datetime.now())
        with transaction.atomic():
            Staff.objects.filter(id=id).update(
                staff_id=data['staff_id'],
                name=data['name'],
                mobile=data['mobile'],
                rf_id=data['rf_id'],
                company_id=data['company'],
                status=data['status'],
                profile_image=img_url,
                update_at=datetime.datetime.now(),
            )
            return JsonResponse({'type': 'success', 'message': 'Staff Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        with transaction.atomic():
            staff = Staff.objects.filter(id=id)
            destination = setting.BASE_DIR + str(staff.first().profile_image)
            if staff.first().profile_image:
                if os.path.isfile(destination):
                    os.remove(staff.first().profile_image.strip("/"))
            staff.delete()
            return JsonResponse({'type': 'success', 'message': 'Staff Deleted Successfully'})


def get_image_url(request, model, method=None, modelData=None):
    data = request.POST
    if request.FILES.get('image', None):
        if modelData:
            if modelData.profile_image:
                destination = setting.BASE_DIR + modelData.profile_image
                if os.path.isfile(destination):
                    os.remove(modelData.profile_image.strip("/"))
                img_url = insert_image(request, model)
            else:
                img_url = insert_image(request, model)
        else:
            img_url = insert_image(request, model)

    else:
        if method == 'update':
            if modelData.profile_image:
                if modelData.profile_image != data['profile_image']:
                    destination = setting.BASE_DIR + modelData.profile_image
                    if os.path.isfile(destination):
                        os.remove(modelData.profile_image.strip("/"))
                img_url = data['profile_image']
            else:
                img_url = data['profile_image']
        else:
            img_url = None
    return img_url


def insert_image(request, model):
    image = request.FILES['image']
    ext = image.name.split('.')[-1]
    image_name = "%s.%s" % (uuid.uuid4(), ext)
    tmp_file = os.path.join(settings.UPLOAD_PATH + '/' + model + '/', image_name)
    path = default_storage.save(tmp_file, ContentFile(image.read()))
    img_url = os.path.join(settings.MEDIA_URL, path)
    return img_url
