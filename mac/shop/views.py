from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse


# Create your views here.
def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("Shop - Contact page")


def tracker(request):
    return HttpResponse("Shop - Tracker page")


def search(request):
    return HttpResponse("Shop - Search page")


def prodview(request):
    return HttpResponse("Shop - Product page")


def checkout(request):
    return HttpResponse("Shop - Checkout page")


def cart(request):
    return HttpResponse("Shop - Cart page")
