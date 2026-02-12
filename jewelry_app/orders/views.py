from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Order


@login_required
def order_list(request):
    orders = Order.objects.filter(is_active=True).order_by("-order_date")

    return render(
        request,
        "order_list.html",
        {"orders": orders}
    )
