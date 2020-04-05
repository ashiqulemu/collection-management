from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('', views.index, name='index'),
    path('get-user', views.get_user, name='get_user'),
    path('create', views.create, name='create'),
    path('store', views.store, name='store'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('change-password', views.change_password, name='change_password'),
    path('change-details', views.change_details, name='change_details'),
]
