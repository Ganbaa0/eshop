from django.shortcuts import get_object_or_404, render
from .cart import Cart
from django.http import JsonResponse, HttpResponseBadRequest
from store.models import Product


def cart(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants()
    return render(request, 'cart.html', {
        'cart_products': cart_products,
        'quantities': quantities,
    })


def cart_add(request):
    if request.POST.get('action') != 'post':
        return HttpResponseBadRequest('Invalid action')

    cart = Cart(request)
    product_id = int(request.POST.get('product_id'))
    product_qty = int(request.POST.get('product_qty'))
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=product_qty)
    cart_quantity = cart.__len__()
    return JsonResponse({'qty': cart_quantity})


def cart_update(request):
    if request.POST.get('action') != 'post':
        return HttpResponseBadRequest('Invalid action')

    cart = Cart(request)
    product_id = int(request.POST.get('product_id'))
    product_qty = int(request.POST.get('product_qty'))
    # засварласан: product_id= → product=
    cart.update(product=product_id, quantity=product_qty)
    return JsonResponse({'qty': product_qty})


def cart_delete(request):
    if request.POST.get('action') != 'post':
        return HttpResponseBadRequest('Invalid action')

    cart = Cart(request)
    product_id = int(request.POST.get('product_id'))
    cart.delete(product=product_id)
    return JsonResponse({'product': product_id})