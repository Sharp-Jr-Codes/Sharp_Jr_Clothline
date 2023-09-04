
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sharpapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('payment/', include('payment.urls')),
]
