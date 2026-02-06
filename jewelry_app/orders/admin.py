from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'agreed_price', 'total_paid', 'pending_balance', 'order_date', 'estimated_delivery_date', 'is_active')
    list_filter = ('status', 'is_active', 'order_date')
    search_fields = ('client__name', 'description', 'product_type')
    readonly_fields = ('created_at', 'updated_at', 'total_paid', 'pending_balance')