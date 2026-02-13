from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["description", "client", "product_type", "status", "order_date", "estimated_delivery_date", "agreed_price"]