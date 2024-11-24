<<<<<<< HEAD
from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm 

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request,'core/signup.html', {
        'form': form
=======
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
>>>>>>> 9197bccd988e4f17a21ca77edeaec7ff2a933e32
    })