from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

# Create your views here.
def Home(request):
    Products = Product.objects.all()
    return render(request, 'store/home.html', {'Products' : Products})

def Product_Details(request, product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'store/product_details.html', {'product' : product})