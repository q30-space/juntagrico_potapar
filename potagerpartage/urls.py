from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impersonate/', include('impersonate.urls')),
    path('', include('juntagrico.urls')),
    path('',include('juntagrico_billing.urls')),
    path('jcr/', include('juntagrico_contribution.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
