from django.urls import path
from . import views

app_name = 'dutyHistory'

urlpatterns = [
    path('', views.index, name='index'),
]