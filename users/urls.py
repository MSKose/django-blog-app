from django.urls import path
from .views import register, profile
from django.contrib.auth import views as auth_views # importing this to use class based LoginView and LogoutView

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'), # specifying template_name cuz I don't want django to look at the default "registration/login.html".
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'), # same goes for this one only this time we'll be directed to django's default admin logout page.
]
