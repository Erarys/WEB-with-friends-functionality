from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import index, RegisterView

app_name = 'accounts'

urlpatterns = [
    path(
        'login/',
        LoginView.as_view(template_name='accounts/login.html'),
        name='login'
    ),
    path(
        'logout/',
        LogoutView.as_view(next_page='login'),
        name='logout'
    ),
    path('register/', RegisterView.as_view(), name='register'),
    path('', index, name='index'),
]
