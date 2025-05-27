from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Review
from decimal import Decimal



def home(request):
    search_query = request.GET.get('q', '')
    category_id = request.GET.get('category')

    categories = Category.objects.all()
    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    if search_query:
        products = products.filter(name__icontains=search_query)

    context = {
        'products': products,
        'categories': categories,
        'selected_category_id': int(category_id) if category_id else None
    }
    return render(request, 'shop/home.html', context)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = category.products.all()
    return render(request, 'shop/category_detail.html', {'category': category, 'products': products})

def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    main_image = product.images.filter(is_main=True).first()
    gallery_images = product.images.exclude(is_main=True)
    reviews = product.reviews.order_by('-date')
    

    context = {
        'product': product,
        'main_image': main_image,
        'gallery_images': gallery_images,
        'reviews': reviews,
    }
    return render(request, 'shop/detail.html', context)


def product_grid(request):
    products = Product.objects.all()
    return render(request, 'shop/product-grid.html', {'products': products})


def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        rating = request.POST.get('rating')
        name = request.POST.get('name')
        email = request.POST.get('email')
        review_text = request.POST.get('review')

        if rating and name and email and review_text:
            Review.objects.create(
                product=product,
                rating=Decimal(rating),
                author=name,
                email=email,
                content=review_text,
            )

    return redirect('shop:product_details', product_id=product.id)


def product_list(request):
    category_id = request.GET.get('category')

    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()

    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }

    return render(request, 'shop/product-list.html', context)
