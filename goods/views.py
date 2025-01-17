from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, render

from goods.models import Products
from goods.utils import q_search


def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    query = request.GET.get('q', None)

    if category_slug =='all':
        goods = Products.objects.all()
    elif query:
        goods =q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug =category_slug))


    paginator = Paginator(goods, 6) #отображается по 3 элемента на странице
    current_page = paginator.page(int(page))
        


    context = {
        "title": "Вкусомания - Каталог",
        "goods": current_page, 
        "slug_url": category_slug
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product=Products.objects.get(slug=product_slug)

    context={
        'product':product
    }
    return render(request, "goods/product.html", context=context)
