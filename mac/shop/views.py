from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return HttpResponse("Shop - About page")


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
