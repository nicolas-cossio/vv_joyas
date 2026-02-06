from django.db import models
from django.forms import ValidationError
from orders.models import Order

# Create your models here.
class Payment(models.Model):
    class Method(models.TextChoices):
        WIRE = 'wire', 'Transferencia'
        CASH = 'cash', 'Efectivo'

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    method = models.CharField(max_length=20, choices=Method.choices, default=Method.WIRE)
    payment_date = models.DateField()
    note = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def clean(self):
        pending = self.order.pending_balance
        
        if self.pk:
            pending += Payment.objects.get(pk=self.pk).amount

        if self.amount > pending:
            raise ValidationError(
                f"El pago de {self.amount} excede el saldo pendiente de {pending}."
            )

    def __str__(self):
        return f"Payment {self.amount} for Order #{self.order.id}"