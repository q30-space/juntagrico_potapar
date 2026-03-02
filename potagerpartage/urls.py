from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impersonate/', include('impersonate.urls')),
    path('', include('juntagrico.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
