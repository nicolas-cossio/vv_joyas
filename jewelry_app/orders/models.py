from django.db import models
from clients.models import Client

# Create your models here.
class Order(models.Model):
    class Status(models.TextChoices):
        QUOTED = 'quoted', 'Cotizado'
        IN_PROGRESS = 'in_progress', 'En proceso'
        READY = 'ready', 'Listo'
        DELIVERED = 'delivered', 'Entregado'
        CANCELLED = 'cancelled', 'Cancelado'

    client = models.ForeignKey(Client, on_delete=models.PROTECT, related_name='orders')
    description = models.TextField()
    product_type = models.CharField(max_length=80, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.QUOTED
    )
    order_date = models.DateField(blank=True, null=True)
    estimated_delivery_date = models.DateField(blank=True, null=True)
    agreed_price = models.DecimalField(max_digits=10, decimal_places=2)

    # TODO Tipo de moneda

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Order #{self.id} - {self.client.name}"

    @property
    def total_paid(self):
        return sum(p.amount for p in self.payments.all())

    @property
    def pending_balance(self):
        return self.agreed_price - self.total_paid  