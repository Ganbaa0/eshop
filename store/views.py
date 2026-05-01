import urllib
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render, get_object_or_404
from .models import Category, Product
from .forms import RegisterForm


def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})


def about(request):
    return render(request, 'about.html', {})


def products_detail(request, pk):
    # get() → get_object_or_404() : бүтээгдэхүүн олдохгүй бол 404 харуулна
    product = get_object_or_404(Product, id=pk)
    return render(request, 'product_detail.html', {'product': product})


def category(request, catname):
    catname = urllib.parse.unquote(catname).replace('-', ' ')
    try:
        category = Category.objects.get(name=catname)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        # Зөвхөн Category.DoesNotExist алдааг барина
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