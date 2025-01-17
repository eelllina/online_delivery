from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories



def index(request):

    context = {
        'title': 'Вкусомания',
        'content': 'Вкусомания — онлайн-магазин с доставкой продуктов и товаров для дома от 15 минут.'
    }
    return render (request, 'main/index.html',context)


def about(request):
   context = {
        'title': 'Home - О нас',
        'content': 'Вкусомания предлагает удобную доставку продуктов и товаров для дома от 15 минут! Наслаждайтесь свежими продуктами и необходимыми вещами, не выходя из дома – всё, что вам нужно, будет доставлено прямо к двери. С нашим быстрым и надежным сервисом вы сможете экономить время и всегда иметь под рукой все самое важное. Сделайте свой день проще с доставкой от Вкусомания!'
    }
   return render (request, 'main/about.html',context)



# Create your views here.
