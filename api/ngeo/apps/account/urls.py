from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("users", views.UserList.as_view(), name="user_list"),
    path("users/<pk>", views.UserDetail.as_view(), name="user_detail"),
]
