from django.urls import path
from .views import LoginPage, logout_page, RegisterPage, activate

app_name = 'users'

urlpatterns = [
    path('login-page/',LoginPage.as_view(),name='login_page'),
    path('logout-page/',logout_page,name='logout_page'), 
    path('register/', RegisterPage.as_view(), name='register_page'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
