from django.urls import path
from .views import customer_list, add_customer, edit_customer, delete_customer, customer_detail, export_data

app_name = 'customers'

urlpatterns = [
    path('customers/', customer_list, name='customer_list'),
    path('customers/add/', add_customer, name='add_customer'),
    path('customers/<int:pk>/edit',  edit_customer, name='edit_customer'),
    path('customers/<int:pk>/delete', delete_customer, name = 'delete_customer'),
    path('customers/<int:pk>/', customer_detail, name='customer_detail'),
    path('export/', export_data, name='export_data'),
]
