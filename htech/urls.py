from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls import url
from .views import (logout, finger)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  # url(r'^admin/', admin.site.urls),
                  url(r'^api/v1/', include('api.urls')),
                  url(r'^accounts/', include('django.contrib.auth.urls')),
                  url(r'^ajax/account/', include('account.urls')),
                  url(r'^ajax/logout', logout, name='logout'),
                  url(r'^finger', finger, name='finger'),
                  url(r'^ajax/company/', include('company.urls')),
                  url(r'^ajax/staff/', include('staff.urls')),
                  url(r'^ajax/guard/', include('guard.urls')),
                  url(r'^ajax/attendance/', include('attendance.urls')),
                  url(r'^ajax/booking/', include('booking.urls')),
                  url(r'^ajax/duty/', include('duty.urls')),
                  url(r'^ajax/building/', include('building.urls')),
                  url(r'^ajax/duty-history/', include('dutyHistory.urls')),
                  url(r'^ajax/report/', include('report.urls')),
                  url(r'^ajax/role/', include('role.urls')),
                  url(r'^ajax/role-user/', include('roleUser.urls')),
                  url(r'^ajax/role-permission/', include('permission.urls')),
                  url(r'^404', TemplateView.as_view(template_name="errors/404.html"), name="403", ),
                  url(r'^403', TemplateView.as_view(template_name="errors/403.html"), name="404", ),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns.append(url(r'^.*$', TemplateView.as_view(template_name="application.html"), name="app", ))
