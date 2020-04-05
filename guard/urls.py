from django.urls import path
from . import views

app_name = 'guard'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]