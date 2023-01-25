from django.urls import path
from apps.order.views import add_to_cart, cart_view, create_order_view


urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('create/', create_order_view, name='create_order'),
]
