from django.urls import path
from .views import signup, profile
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView
)

urlpatterns = [

    path(
        'login/',
        LoginView.as_view(
            template_name='registration/login.html'
        ),
        name='login'
    ),

    path('signup/', signup, name='signup'),

    path('profile/', profile, name='profile'),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),

    path(
        'password-reset/',
        PasswordResetView.as_view(
            template_name='registration/password_reset.html'
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

]