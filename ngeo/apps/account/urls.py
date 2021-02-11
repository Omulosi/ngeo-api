from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views

urlpatterns = [
    path("auth/me", views.Me.as_view(), name="me"),
    path("users", views.UserList.as_view(), name="user_list"),
    path("auth/signup", views.UserCreate.as_view(), name="signup"),
    path("auth/login", views.UserLogin.as_view(), name="login"),
    # path(
    # "auth/forgot-password",
    # views.UserForgotPassword.as_view(),
    # name="forgot_password",
    # ),
    # path(
    # "auth/reset-password", views.UserResetPassword.as_view(), name="reset_password"
    # ),
]
