from django.shortcuts import render
from product.models import Category, Product

def index(request):
    products = Product.objects.filter(is_sold=False)
    latest_products = Product.objects.order_by('-date_added')[:3]
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'categories': categories,
        'products': products,
        'latest_products': latest_products,
    })