from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# такая функция в файле views называется представлением или контроллером
def index(request):
    context = {
        "title": "Home",
        "content": "Код написан, только непонятно почему номер текущей",
        "list": ["first", "second"],
        "dict": {"first": 1},
        "is_auth": False,
    }
    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
