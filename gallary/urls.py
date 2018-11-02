from django.urls import path
from . import views


urlpatterns = [
    path('<int:gallary_id>/', views.page),
]