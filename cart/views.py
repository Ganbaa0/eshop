from django.shortcuts import get_object_or_404, render
from .cart import Cart
from django.http import JsonResponse
from store.models import Product
 
# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    return render(request, 'cart.html', {'cart_products': cart_products})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        response = JsonResponse({'Product_name': product.name})
        return response