from django.urls import path
from .views import customer_list, add_customer, edit_customer, delete_customer, customer_detail, login_page, logout_page, register_page

app_name = 'users'

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('customers/add/', add_customer, name='add_customer'),
    path('customers/<int:pk>/edit',  edit_customer, name='edit_customer'),
    path('customers/<int:pk>/delete', delete_customer, name = 'delete_customer'),
    path('customers/<int:pk>/', customer_detail, name='customer_detail'),
    path('login-page/',login_page,name='login_page'),
    path('logout-page/',logout_page,name='logout_page'), 
    path('register/', register_page, name='register_page'),

]
