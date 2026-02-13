from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .form import OrderForm
from .models import Order


@login_required
def order_list(request):
    orders = Order.objects.filter(is_active=True).order_by("-order_date")

    return render(request, "order_list.html", {"orders": orders})

# Create a new order
@login_required
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm()

    return render(request, "order_form.html", {"form": form})

# View order details
@login_required
def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    payments = order.payments.all()

    return render(request, "order_detail.html", {"order": order, "payments": payments})

# Update an existing order
@login_required
def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)

    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("order_list")
    else:
        form = OrderForm(instance=order)

    return render(request, "order_form.html", {"form": form})