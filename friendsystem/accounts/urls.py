from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import HomePageView, RegisterView, UpdatePersonalPage

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
    path('update/', UpdatePersonalPage.as_view(), name='update'),
    path('', HomePageView.as_view(), name='profile'),
]
