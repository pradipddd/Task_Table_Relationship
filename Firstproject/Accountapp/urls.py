from django.urls import path
from .views import Userregister,Userlogin,Userlogout

urlpatterns=[
    path('register/',Userregister,name='register'),
    path('login/',Userlogin,name='login'),
    path('logout/',Userlogout,name='logout')
]