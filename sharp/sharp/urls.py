
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sharpapp.urls')),
    path('sharpauth/', include('sharpauth.urls')),
]
