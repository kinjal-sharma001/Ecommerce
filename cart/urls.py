from django.urls import path
from .views import Cart, Add_To_Cart, Remove_To_Cart, Add_To_Cart_on_cart_page

urlpatterns = [
    path('', Cart, name='cart'),
    path('add/<int:product_id>/', Add_To_Cart, name='add'),
    path('remove/<int:product_id>/', Remove_To_Cart, name='remove'),
    path('addOnCart/<int:product_id>/', Add_To_Cart_on_cart_page, name='addOnCart'),
]