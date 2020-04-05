from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [
    path('dashboard-report', views.dashboard_report, name='dashboard_report'),

]
