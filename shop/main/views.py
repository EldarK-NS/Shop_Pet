from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories


# Create your views here.
# такая функция в файле views называется представлением или контроллером
def index(request):
    # categories = Categories.objects.all()
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        # "categories": categories,
    }
    return render(request, "main/index.html", context)


def about(request):

    context = {
        "title": "Home - - О нас",
        "content": "О нас",
        "text_on_page": "Браузерные и клиентские онлайн-игры",
    }
    return render(request, "main/about.html", context)
