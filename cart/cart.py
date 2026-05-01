from store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session
        # одоогийн сешний түлхүүрийг авна
        cart = self.session.get('session_key')

        # Хэрэв сешний түлхүүр байхгүй бол үүсгэж өгнө
        if 'session_key' not in self.session:
            cart = self.session['session_key'] = {}

        # Сагс бүх хуудсанд байгааг баталгаажуулах
        self.cart = cart

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        if product_id not in self.cart:
            # self.cart[product_id] = {'price': str(product.price)}
            self.cart[product_id] = int(product_qty)
        else:
            pass
            # self.cart[product_id]['quantity'] = str(int(self.cart[product_id]['quantity']) + quantity)

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        # Сагсны бүх бүтээгдэхүүний ID-г авна
        product_ids = self.cart.keys()
        # Сагсны бүх бүтээгдэхүүнийг өгөгдлийн сангаас авна
        products = Product.objects.filter(id__in=product_ids)
        return products
    
    def get_quants(self):
        quanties = self.cart
        return quanties
    
    def update(self, product, quantity):
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id] = int(quantity)
            self.session.modified = True
            return self.cart
    
    def delete(self, product):
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
        
        self.session.modified = True