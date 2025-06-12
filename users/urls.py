from django.urls import path
from .views import login_page, logout_page, register_page

app_name = 'users'

urlpatterns = [
    path('login-page/',login_page,name='login_page'),
    path('logout-page/',logout_page,name='logout_page'), 
    path('register/', register_page, name='register_page'),
]
