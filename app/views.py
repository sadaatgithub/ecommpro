from django.http.request import HttpRequest
from django.shortcuts import render
from .models import Product,Category
# Create your views here.

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'app/home.html', {'products': products})



