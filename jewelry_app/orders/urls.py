from django.urls import path
from .views import order_list, order_create, order_detail, order_update

urlpatterns = [
    path("", order_list, name="order_list"),
    path("new/", order_create, name="order_create"),
    path("<int:pk>/detail/", order_detail, name="order_detail"),
    path("<int:pk>/edit/", order_update, name="order_update"),
]
