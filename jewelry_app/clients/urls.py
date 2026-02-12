from django.urls import path
from .views import client_create, client_list, client_update

urlpatterns = [
    path("", client_list, name="client_list"),
    path("new/", client_create, name="client_create"),
    path("<int:pk>/edit/", client_update, name="client_update"),
]
