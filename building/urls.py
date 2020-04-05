from django.urls import path
from . import views

app_name = 'building'

urlpatterns = [
    path('', views.index, name='index'),
    path('store', views.store, name='store'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]
