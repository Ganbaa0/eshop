from django.contrib import messages

from django.shortcuts import redirect, render
import urllib
from .models import Category, Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def products_detail(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'product_detail.html', {'product': product})

def category(request, catname):
    catname = urllib.parse.unquote(catname).replace('-', ' ')
    try:
        category = Category.objects.get(name=catname)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except:
        messages.success(request, 'Тохирох ангилал олдсонгүй')
        return redirect('home')