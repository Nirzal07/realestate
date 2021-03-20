from django.urls import path
from . import views
app_name= 'userapp'

urlpatterns= [
    path('login', views.user_login, name= 'user_login'),
    path('register', views.register, name= 'register'),
    path('logout', views.user_logout, name= 'user_logout'),
    path('profile', views.user_profile, name='profile')
]