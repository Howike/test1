from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='注册页面'),
    path('login/', views.login, name='登陆页面'),
    path('logout/', views.logout, name='退出页面'),
    path('publish/', views.publish, name='发布页面'),
    path('<int:article_id>/', views.article)
]