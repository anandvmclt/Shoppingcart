from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about', views.about, name="AboutUS"),
    path('contact', views.contact, name="contactUS"),
    path('tracker', views.tracker, name="trackingStatus"),
    path('search', views.search, name="search"),
    path('productview', views.prodview, name="productview"),
    path('checkout', views.checkout, name="checkout"),
    path('cart', views.cart, name="cart"),
]