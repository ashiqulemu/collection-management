from django.urls import path
from . import views

app_name = 'roleUser'

urlpatterns = [
    path('get-role-user', views.index, name='index'),
    path('assign-role', views.assign, name='assign'),
]