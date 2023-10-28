from rest_framework.authtoken import views as views_token
from . import views 
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signin/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views_token.obtain_auth_token , name='login')
]