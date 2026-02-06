from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'amount', 'method', 'payment_date', 'is_active')
    list_filter = ('method', 'payment_date', 'is_active')
    search_fields = ('order__id', 'amount')
    ordering = ('-payment_date',)