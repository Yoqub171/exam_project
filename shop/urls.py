from django.urls import path
from .views import Home, ProductDetail, ProductList, ProductGrid, CategoryDetail, AddReview
from django.conf import settings
from django.conf.urls.static import static

app_name = 'shop'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('product/<int:product_id>/', ProductDetail.as_view(), name='product_details'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('product-grid/', ProductGrid.as_view(), name='product_grid'),
    path('category/<int:pk>/', CategoryDetail.as_view(), name='category_detail'),
    path('product/<int:product_id>/add_review/', AddReview.as_view(), name='add_review'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
