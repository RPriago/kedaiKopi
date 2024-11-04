from django.shortcuts import render
from product.models import Category, Product

def index(request):
    products = Product.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'categories': categories,
        'products': products,
    })