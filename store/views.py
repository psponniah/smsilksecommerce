from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import category

# Create your views here.
def store(request , category_slug = None):
    products = None
    categories = None
    if category_slug != None:

        categories = get_object_or_404(category , slug = category_slug)
        products  = Product.objects.filter(is_available =True, category = categories)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()


    context = {
        'products' : products ,
        'product_count' : product_count,
    }
    return render(request, 'store/store.html',context)


def product_detail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug = category_slug , slug = product_slug)

    except Exception as e:
        raise e

    context = {
        'product' : product,
    }
    return render(request,'store/product_detail.html', context)
