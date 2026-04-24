from .cart import Cart

def cart(request):
    # Сагсыг бүх хуудсанд байгааг баталгаажуулах
    return {'cart': Cart(request)}