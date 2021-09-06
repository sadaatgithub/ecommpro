from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404, render
from .models import Product,Category
from django.contrib.auth.decorators import login_required
# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }
def home(request):
    products = Product.objects.all()
    return render(request, 'app/home.html', {'products': products})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'app/product/all_products.html', {'products': products})

def ProductDetail(request,slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'app/product/detail.html', {'product':product})

def category_list(request,category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'app/product/category.html',{'category':category, 'product':product})



