from django.contrib import admin
from .models import Customer
from import_export.admin import ExportMixin



@admin.register(Customer)
class CustomerAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'address', 'joined')
    search_fields = ('full_name', 'email')
    list_filter = ('joined',)

