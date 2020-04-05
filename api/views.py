from booking.views import store as BookingAPIStore, index as BookingList, create as BookingAPICreate, \
    edit as BookingAPIEdit, update as BookingAPIUpdate, delete as BookingAPIDelete
from company.views import index as CompanyList, store as CompanyAPIStore, create as CompanyAPICreate, \
    edit as CompanyAPIEdit, update as CompanyAPIUpdate, delete as CompanyAPIDelete
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication

from htech.globalMethods import getUserByToken
from htech.serializers import LoginSerializer


class BookingView(APIView):
    @classmethod
    def get(self, request):
        return BookingList(request)


class BookingEdit(APIView):
    @classmethod
    def get(self, request, id):
        return BookingAPIEdit(request, id)


class BookingCreate(APIView):
    @classmethod
    def get(self, request):
        return BookingAPICreate(request)


class BookingStore(APIView):
    @classmethod
    def post(self, request):
        user_id = request.session.get('user_id', None)
        return BookingAPIStore(request, user_id)


class BookingUpdate(APIView):
    @classmethod
    def patch(self, request, id):
        return BookingAPIUpdate(request, id)


class BookingDelete(APIView):
    @classmethod
    def delete(self, request, id):
        return BookingAPIDelete(request, id)


class CompanyView(APIView):
    @classmethod
    def get(self, request):
        return CompanyList(request)


class CompanyEdit(APIView):
    @classmethod
    def get(self, request, id):
        return CompanyAPIEdit(request, id)


class CompanyCreate(APIView):
    @classmethod
    def get(self, request):
        return CompanyAPICreate(request)


class CompanyStore(APIView):
    @classmethod
    def post(self, request):
        return CompanyAPIStore(request)


class CompanyUpdate(APIView):
    @classmethod
    def patch(self, request, id):
        return CompanyAPIUpdate(request, id)


class CompanyDelete(APIView):
    @classmethod
    def delete(self, request, id):
        return CompanyAPIDelete(request, id)


class LoginView(APIView):
    @classmethod
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        django_logout(request)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    @classmethod
    def post(self, request):
        django_logout(request)
        return Response(status=204)
