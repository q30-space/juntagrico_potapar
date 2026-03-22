from django.urls import path, include
from django.contrib import admin
from juntagrico.views import create_subscription

from potagerpartage.utils import next_wednesday

urlpatterns = [
    path('admin/', admin.site.urls),
    path('impersonate/', include('impersonate.urls')),
    path('subscription/create/start/', create_subscription.select_start_date,
         {'default': next_wednesday}, name='cs-start'),
    path('', include('juntagrico.urls')),
    path('',include('juntagrico_billing.urls')),
    path('jcr/', include('juntagrico_contribution.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]
