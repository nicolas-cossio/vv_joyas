from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'note', 'created_at', 'updated_at', 'is_active')
    search_fields = ('name', 'phone_number', 'email')
    list_filter = ('is_active', 'created_at')
    ordering = ('name',)