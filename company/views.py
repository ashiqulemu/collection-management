from django.contrib.auth.models import User

from building.models import Building
from role.views import permission_create
from roleUser.models import RoleUser
from company.models import Company
from htech.globalMethods import GetListData
import json
from django.http import JsonResponse
import datetime
from django.db import transaction
from htech.serializers import CompanySerializer
from role.models import Role


def index(request):
    company = GetListData()
    data = company.get(request, Company.objects.all(), CompanySerializer, 'Company')
    return JsonResponse({
        'data': data[0],
        'totalItems': data[1],
    })


def create(request):
    building = Building.objects.all()
    return JsonResponse({
        'building': list(building.values()),
    })


def store(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        with transaction.atomic():
            user_name = data['company']['name'].replace(" ", "")
            new_user = User.objects.create_user(username=user_name.lower(),
                                                email=data['company']['email'],
                                                password=123456,
                                                is_active=data['company']['status'] == 'Active' if 1 else 0
                                                )
            Company.objects.create(
                name=data['company']['name'],
                authorize_person=data['company']['authorize_person'],
                owner=data['company']['owner'],
                building_id=data['company']['building'],
                email=data['company']['email'],
                mobile=data['company']['mobile'],
                status=data['company']['status'],
                user_id=new_user.id,
                update_at=datetime.datetime.now(),
                created_at=datetime.datetime.now()
            )
            role_user = Role.objects.filter(name__icontains='Company')
            if role_user:
                RoleUser.objects.create(
                    role_id=role_user.first().id,
                    user_id=new_user.id
                )
            else:
                new_role = Role.objects.create(name='Company')
                permission_create(new_role.id)

                RoleUser.objects.create(
                    role_id=new_role.id,
                    user_id=new_user.id
                )
            return JsonResponse({'type': 'success', 'message': 'Company Created Successfully'})


def edit(request, id):
    building = Building.objects.all()
    company = Company.objects.filter(id=id).values()
    return JsonResponse({
        'result': list(company)[0],
        'building': list(building.values()),
    })


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        with transaction.atomic():
            company = Company.objects.filter(id=id)
            company.update(
                name=data['company']['name'],
                owner=data['company']['owner'],
                authorize_person=data['company']['authorize_person'],
                building_id=data['company']['building'],
                email=data['company']['email'],
                mobile=data['company']['mobile'],
                status=data['company']['status'],
                update_at=datetime.datetime.now(),
            )

            User.objects.filter(id=company.first().user_id).update(
                is_active=data['company']['status'] == 'Active' if 1 else 0
            )

            return JsonResponse({'type': 'success', 'message': 'Company Update Successfully'})


def delete(request, id):
    if request.method == 'DELETE':
        company = Company.objects.filter(id=id)
        if company.first().user_id:
            User.objects.filter(id=company.first().user_id).delete()
        company.delete()
        return JsonResponse({'type': 'success', 'message': 'Company Deleted Successfully'})


def get_company(request):
    if request.method == 'GET':
        v = request.GET.get('name')
        companies = Company.objects.filter(name__icontains=v, status__exact='Active')[: 2]
        return JsonResponse({
            'companies': list(companies.values()),
        })
