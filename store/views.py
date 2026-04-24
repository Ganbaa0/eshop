from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
import urllib
from .models import Category, Product
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .forms import RegisterForm

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
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Амжилттай нэвтэрлээ')
            return redirect('home')
        else:
            messages.error(request, 'Нэвтрэх нэр эсвэл нууц үг буруу байна')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Амжилттай гарлаа')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Бүртгүүлсэнд баярлалаа. Одоо нэвтэрнэ үү.')
            return redirect('login')
        else:
            messages.error(request, 'Бүртгүүлэхэд алдаа гарлаа. Мэдээллээ шалгаад дахин оролдоно уу.')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})