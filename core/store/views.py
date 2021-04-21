from django.shortcuts import render
from .models import Category, Product


def all_product(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store/home.html', context)