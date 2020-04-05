from django.urls import path

from .views import (LoginView, LogoutView, BookingStore, CompanyView, CompanyStore, CompanyCreate, BookingView,
                    BookingCreate, BookingEdit, CompanyUpdate, BookingUpdate, CompanyEdit, CompanyDelete, BookingDelete)
from django.views.decorators.csrf import csrf_exempt

app_name = 'api'

urlpatterns = [
    path('auth/login', csrf_exempt(LoginView.as_view())),
    path('auth/logout', csrf_exempt(LogoutView.as_view())),
    path('company', CompanyView.as_view()),
    path('booking', BookingView.as_view()),
    path('company/create', CompanyCreate.as_view()),
    path('company/store', csrf_exempt(CompanyStore.as_view())),
    path('company/<int:id>/edit', CompanyEdit.as_view()),
    path('company/<int:id>/update', csrf_exempt(CompanyUpdate.as_view())),
    path('company/delete/<int:id>', CompanyDelete.as_view()),
    path('booking/create', BookingCreate.as_view()),
    path('booking/store', csrf_exempt(BookingStore.as_view())),
    path('booking/<int:id>/edit', BookingEdit.as_view()),
    path('booking/<int:id>/update', csrf_exempt(BookingUpdate.as_view())),
    path('booking/delete/<int:id>', BookingDelete.as_view()),
]
