from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect
    


admin.site.site_header = "SHARPJr."
admin.site.site_title = "Sharp"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sharpapp.urls')),
    path('accounts/', include('accounts.urls')),
    path('payment/', include('payment.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
