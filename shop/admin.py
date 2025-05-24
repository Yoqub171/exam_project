from django.contrib import admin
from .models import Product, Category, Order, Comment
from django.contrib.auth.models import User,Group
from adminsortable2.admin import SortableAdminMixin
from import_export.admin import ExportMixin, ImportExportModelAdmin
from import_export import resources


# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Order)

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class ProductInline(admin.StackedInline):
    model = Product
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name',]
    inlines = [
        ProductInline,
    ]

@admin.register(Product)
class ProductAdmin(SortableAdminMixin, ImportExportModelAdmin,  admin.ModelAdmin):
    list_display = ['name', 'price', 'discount', 'category', 'my_order']
    search_fields = ['name']
    list_filter = ['price', 'category']


# admin.site.unregister(User)
# admin.site.unregister(Group)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'text', 'rating', 'created_at')
    search_fields = ('user__username', 'text') 

admin.site.register(Comment, CommentAdmin)
