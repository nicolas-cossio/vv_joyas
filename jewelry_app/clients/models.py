from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    note = models.TextField(blank=True)

    # Audit fields (Always on every model)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name