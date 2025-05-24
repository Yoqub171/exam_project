from django.urls import path
from .views import home, product_detail, order_detail, category_detail, product_list, product_grid
from django.conf import settings
from django.conf.urls.static import static


app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('order/detail/<int:pk>/', order_detail, name='order_detail'),
    path('category/<int:id>/',  category_detail, name='category_detail'),
    path('product-list/', product_list, name='product_list'),
    path('product-grid/', product_grid, name='product_grid'),

]

