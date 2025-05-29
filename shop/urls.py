from django.urls import path
from .views import home, product_details, product_list, product_grid, category_detail, add_review
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:product_id>/', product_details, name='product_details'),
    path('products/', product_list, name='product_list'),
    path('product-grid/', product_grid, name='product_grid'),
    path('category/<int:pk>/', category_detail, name='category_detail'),
    path('product/<int:product_id>/add_review/', add_review, name='add_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
