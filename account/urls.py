from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.login, name='登陆页面'),
    path('loginup/', views.signup, name='注册页面'),
]