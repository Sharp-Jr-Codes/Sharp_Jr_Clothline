from django.urls import path
from payment import views

urlpatterns = [
    path('mpesa/', views.mpesa, name='mepesa')
]
