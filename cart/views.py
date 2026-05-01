from django.shortcuts import get_object_or_404, render
from .cart import Cart
from django.http import JsonResponse
from store.models import Product
 
# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    return render(request, 'cart.html', {'cart_products': cart_products, 'quantities': quantities})
    # return render(request, 'cart.html', {'cart_products': cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        # response = JsonResponse({'Product_name': product.name})
        cart_quantity = cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
        return response

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        cart.update(product_id=product_id, quantity=product_qty)
        response = JsonResponse({'qty': product_qty})
        return response
    
def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product_id=product_id)
        response = JsonResponse({'product': product_id})
        return response