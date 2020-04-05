from django.urls import path
from . import views

app_name = 'permission'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
]