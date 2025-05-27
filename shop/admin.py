from django.contrib import admin
from .models import Product, Category, ProductImage, Review
from adminsortable2.admin import SortableAdminMixin
from import_export.admin import ImportExportModelAdmin


class ProductImageInline(admin.TabularInline): 
    model = ProductImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Product)
class ProductAdmin(SortableAdminMixin, ImportExportModelAdmin):
    list_display = ['name', 'price', 'discount', 'category', 'my_order']
    search_fields = ['name']
    list_filter = ['price', 'category']
    inlines = [ProductImageInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rating', 'date')
    search_fields = ('author', 'content')
    list_filter = ('rating', 'date')

# admin.site.register(Product, ProductAdmin)
