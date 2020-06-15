from django.shortcuts import render
from .models import Product
from math import ceil
from django.http import HttpResponse


# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    #  n = len(products)

    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1, nSlides), nSlides])
    #params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    #allProds = [[products, range(1, nSlides), nSlides],
    #            [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
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
