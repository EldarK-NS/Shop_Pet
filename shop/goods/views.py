from django.shortcuts import render

# Create your views here.
#! Controllers


def catalog(request):
    return render(request, "goods/catalog.html")


def product(request):
    return render(request, "goods/product.html")
