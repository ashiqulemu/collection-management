from django.contrib.auth.models import User
from django.core.paginator import Paginator
from rest_framework.views import APIView

from role.models import Role
from .models import Permission
import json
from django.http import JsonResponse
from django.db.models import F, Count, Q


def index(request):
    query = Permission.objects.all().values('user_id').annotate(dcount=Count('user_id'),
                                                                first_name=F('user__first_name'),
                                                                last_name=F('user__last_name'),
                                                                role=F('role__role')).values('user_id', 'first_name',
                                                                                             'last_name', 'role')
    permission = GetPermissionLIst()
    data = permission.get(request, query)
    return JsonResponse({
        'data': list(data[0]),
        'pagination': data[1],
    })


def edit(request, id):
    permissions = Permission.objects.filter(role_id=id).values()
    roles = Role.objects.all().values()
    return JsonResponse({
        'result': list(permissions),
        'roles': list(roles)
    })


def update(request, id):
    if request.method == 'PATCH':
        data = json.loads(request.body)
        field = data['field']

        if field == 'create_permission':
            Permission.objects.filter(id=data['id']).update(create_permission=data['value'])
        if field == 'edit_permission':
            Permission.objects.filter(id=data['id']).update(edit_permission=data['value'])
            Permission.objects.filter(id=data['id']).update(view_permission=1)

        if field == 'view_permission':
            permission = Permission.objects.filter(id=data['id']).first()
            if not permission.edit_permission and not permission.delete_permission and not permission.share_permission:
                Permission.objects.filter(id=data['id']).update(view_permission=data['value'])
            else:
                return JsonResponse({'type': 'error', 'message': 'For Edit, Delete or share need to view, '
                                                                 'Please Remove permission Edit, Delete and Share first'})

        if field == 'delete_permission':
            Permission.objects.filter(id=data['id']).update(delete_permission=data['value'])
            Permission.objects.filter(id=data['id']).update(view_permission=1)
        if field == 'share_permission':
            Permission.objects.filter(id=data['id']).update(share_permission=data['value'])
            Permission.objects.filter(id=data['id']).update(view_permission=1)

        return JsonResponse({'type': 'success', 'message': 'Permission Update Successfully'})


class GetPermissionLIst(APIView):

    def get(self, request, query):
        v = request.GET.get('searchValue')
        p = None
        if request.GET.get('searchValue'):
            query = query.filter(Q(user__first_name__icontains=v) | Q(user__last_name__icontains=v))
        if request.GET.get('rowsPerPage'):
            p = Paginator(query, request.GET.get('rowsPerPage'))

        data = p.page(int(request.GET.get('page')))

        return [data, pagination(p, data, request)]


def pagination(p, data, request):
    paging = {}
    paging['current_page'] = int(request.GET.get('page'))
    paging['from'] = data.start_index()
    paging['to'] = data.end_index()
    paging['per_page'] = p.per_page
    paging['total'] = p.count
    last_page = paging['total'] / paging['per_page']
    if int(last_page) < float(last_page):
        last_page = int(last_page) + 1
    else:
        last_page = int(last_page)
    paging['last_page'] = last_page
    return paging
