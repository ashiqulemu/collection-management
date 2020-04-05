from django.contrib.auth.models import User
from django.shortcuts import redirect
from rest_framework.authentication import TokenAuthentication

from htech.globalMethods import hasRoleId, hasRole
from htech.guardMiddleWare import check_guard_schedule
from permission.models import Permission
from rest_framework.authtoken.models import Token


class CheckPageAccessMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, *view_args, **view_kargs):
        path = request.get_full_path()
        if not '/api/v1/' in path:
            if not request.user.id:
                if path != '/accounts/login/':
                    response = redirect('/accounts/login/')
                    return response
            else:

                if path == '/accounts/login/':
                    response = redirect('/dashboard')
                    return response
                if not request.user.is_superuser:
                    response = redirect('/403')
                    permission = Permission.objects.filter(role_id=hasRoleId(request))

                    if path != '/ajax/account/get-user':

                        for item in permission:
                            if item.moduled.lower() == 'company' in path:
                                return goOr403('/company', path, item, response, '/company', request)
                            elif item.moduled.lower() == 'booking' in path:
                                return goOr403('/booking', path, item, response, '/booking', request)
                            elif item.moduled.lower() == 'attendance' in path:
                                return goOr403('/attendance', path, item, response, '/attendance', request)
                            elif item.moduled.lower() == 'staff' in path:
                                return goOr403('/staff', path, item, response, '/staff', request)
                            elif item.moduled.lower() == 'building' in path:
                                return goOr403('/building', path, item, response, '/building', request)
                            elif item.moduled.lower() == 'guard' in path:
                                return goOr403('/guard', path, item, response, '/guard', request)
                            elif item.moduled.lower() == 'duty' in path and not 'duty-history' in path:
                                return goOr403('/duty', path, item, response, '/duty', request)
                            elif item.moduled.lower() == 'duty-history' in path:
                                return goOr403('/duty-history', path, item, response, '/duty-history', request)
                            elif item.moduled.lower() == 'user' in path:
                                return goOr403('/user', path, item, response, '/user', request)
                            elif item.moduled.lower() == 'role-permission' and 'role' in path:
                                return goOr403('/role', path, item, response, '/role', request)
        else:
            if not '/api/v1/auth' in path:
                access_token = request.META.get('HTTP_AUTHORIZATION', '')
                access_token = access_token.replace("Bearer ", "")

                if access_token:
                    access_token = Token.objects.filter(key=access_token).first()
                    if access_token:
                        user = User.objects.filter(id=access_token.user_id, is_active=1).first()
                        if user.id:
                            request.session['user_id'] = user.id
                            access_token = True
                        else:
                            access_token = False
                    else:
                        access_token = False
                else:
                    access_token = False

                if not access_token:
                    response = redirect('/403')
                    return response


def goOr403(model, path, item, response, view_page, request):
    if hasRole(request) == 'Guard':
        if not check_guard_schedule(request):
            if '/duty-history' in path:
                return response
            else:
                if not '/duty' in path:
                    return response
                else:
                    if view_page in path:
                        if not item.view_permission:
                            return response
    if view_page in path:
        if not item.view_permission:
            return response

    if model + '/create' in path:
        if not item.create_permission:
            return response
    if model in path:
        if '/edit' in path:
            if not item.edit_permission:
                return response
    if model in path:
        if '/update' in path:
            if not item.edit_permission:
                return response
    if model in path:
        if '/delete' in path:
            if not item.delete_permission:
                return response

    if model in path:
        if '/show' in path:
            if not item.view_permission:
                return response

