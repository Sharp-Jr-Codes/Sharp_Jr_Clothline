from django.urls import path
from sharpapp import views

urlpatterns = [
    path('sugnup/', views.signup, name='signup')
]
