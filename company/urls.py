from django.urls import path
from . import views

app_name = 'company'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('get-company', views.get_company, name='get_company'),
]
