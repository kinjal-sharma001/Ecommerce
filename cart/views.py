from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from store.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Cart(request):
    cart_items = Item.objects.filter(user = request.user)
    return render(request, 'cart/cart.html', {'cart_items' : cart_items})


@login_required
def Add_To_Cart(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    cart_item, created = Item.objects.get_or_create(user = request.user ,product = product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('home')

def Add_To_Cart_on_cart_page(request, product_id):
    product = get_object_or_404(Product, id = product_id)
    cart_item, created = Item.objects.get_or_create(user = request.user ,product = product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def Remove_To_Cart(request, product_id):
    cart_item = Item.objects.filter(product_id = product_id).first()
    if cart_item:
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')
        
def Cart_Length(request):
    if request.user.is_authenticated:
        count = Item.objects.filter(user = request.user).count()

    else:
        count = 0
    return {'count': count}