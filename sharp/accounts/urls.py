from django.urls import path
from accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.handlelogin, name='hundlelogin'),
    path('logout/', views.handlelogout, name='handlelogout')
]
