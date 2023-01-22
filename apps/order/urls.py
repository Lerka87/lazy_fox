from django.urls import path
from apps.order.views import add_to_cart, cart


urlpatterns = [
    path('', cart, name='cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
]
