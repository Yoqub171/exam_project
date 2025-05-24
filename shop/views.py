from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Product, Category
from .forms import OrderForm


def home(request, category_id=None):
    search_query = request.GET.get('q', '')
    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    if search_query:
        products = products.filter(name__icontains=search_query)

    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        related_products = Product.objects.filter(category = product.category).exclude(id = product.id)
        form = OrderForm()

        context = {
            'product': product,
            'form': form,
            'related_products': related_products
        }
        return render(request, 'shop/detail.html', context)
    
    except Product.DoesNotExist:
        return HttpResponse('Product Not Found')
    

def order_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = OrderForm()

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)
            order.product = product

            if product.quantity < order.quantity or order.quantity == 0:
                messages.add_message(
                    request,
                    messages.ERROR,
                    'Dont have enough product quantity'
                )
            else:
                product.quantity -= order.quantity
                product.save()

                order.save()

                messages.add_message(
                    request,
                    messages.SUCCESS,
                    'Item successfully ordered'
                )

                return redirect('shop:product_detail', pk=product.pk)

    context = {
        'form': form,
        'product': product
    }

    return render(request, 'shop/detail.html', context)

def category_detail(request, id):
    category = get_object_or_404(Category, id=id)
    products = Product.objects.filter(category=category)
    categories = Category.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'active_category': category
    }
    
    return render(request, 'shop/home.html', context)


def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/product-list.html', {'products': products, 'categories': categories})


def product_grid(request):
    return render(request, 'shop/product-grid.html')
