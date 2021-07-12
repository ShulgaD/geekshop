import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from mainapp.models import Product, ProductCategory


# Create your views here.
# def get_menu():
#     return ProductCategory.objects.all()


def get_hot_product():
    # product_id = Product.objects.values_list('id', flat=True).all()
    # random_id = random.choice(product_id)
    # return Product.objects.get(pk=random_id)
    return random.choice(Product.objects.all())


def same_products(hot_product):
    return Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)


def index(request):
    date_val = datetime.now()
    context = {
        'page_title': 'главная',
        'date_val': date_val
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    hot_product = get_hot_product()
    context = {
        'page_title': 'товары',
        'hot_product': hot_product,
        'same_products': same_products(hot_product),
        # 'categoryes': get_menu(),
    }
    return render(request, 'mainapp/products.html', context)


def page_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'page_title': 'страница продукта',
        'product': product,
        # 'categoryes': get_menu(),
    }
    return render(request, 'mainapp/page_product.html', context)


def category(request, pk):
    page_num = request.GET.get('page', 1)
    if pk == 0:
        category = {'pk': 0, 'name': 'все'}
        products = Product.objects.all()
    else:
        category = ProductCategory.objects.filter(pk=pk).first()
        products = category.product_set.all()

    products_paginator = Paginator(products, 3)
    try:
        products = products_paginator.page(page_num)
    except PageNotAnInteger:
        products = products_paginator.page(1)
    except EmptyPage:
        products = products_paginator.page(products_paginator.num_pages)

    context = {
        'page_title': 'товары категории',
        'category': category,
        'products': products,
        # 'categoryes': get_menu(),
    }
    return render(request, 'mainapp/category_products.html', context)


def contact(request):
    contacts = [
        {'city': 'Москва',
         'phone': '+7-900-111-11-11',
         'email': 'info@chairs.ru',
         'addres': 'В пределах МКАД'
         },
        {'city': 'Санкт_Петербург',
         'phone': '+7-900-222-22-22',
         'email': 'info-spb@chairs.ru',
         'addres': 'В пределах КАД'
         },
        {'city': 'Кингисепп',
         'phone': '+7-900-333-33-33',
         'email': 'info-king@chairs.ru',
         'addres': 'В пределах центра'
         },
    ]
    context = {
        'page_title': 'контакты',
        'contacts': contacts,
    }
    return render(request, 'mainapp/contact.html', context)
