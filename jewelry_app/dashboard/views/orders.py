from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from orders.models import Order


@login_required
def order_list(request):
    orders = Order.objects.filter(is_active=True).order_by("-order_date")

    return render(
        request,
        "dashboard/order_list.html",
        {"orders": orders}
    )
