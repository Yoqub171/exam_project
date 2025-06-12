from django.contrib import admin
from .models import Product, Category, ProductImage, Review, Attribute, AttributeKey, AttributeValue
from adminsortable2.admin import SortableAdminMixin
from import_export.admin import ImportExportModelAdmin

# class ProductSpecificationInline(admin.StackedInline):
#     model = ProductSpecification
#     can_delete = False
#     verbose_name_plural = 'Specifications'

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'price', 'discount', 'category', 'my_order']
    search_fields = ['name']
    list_filter = ['price', 'category']

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['name', 'image', 'slug']
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rating', 'date')
    search_fields = ('author', 'content')
    list_filter = ('rating', 'date')


admin.site.register(Attribute)
admin.site.register(AttributeKey)
admin.site.register(AttributeValue)