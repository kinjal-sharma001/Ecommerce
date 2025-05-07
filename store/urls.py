from django.urls import path
from .views import Home, Product_Details

urlpatterns = [
    path('', Home, name='home'),
    path('product_details/<int:product_id>/', Product_Details, name='product_details'),
]
