from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='AboutUs'),
    path('contact/', contact, name='MyContact'),
    path('search/', search, name='search'),
    path('profile/', profile, name='MyProfile'),
    path('tracker/<slug:order_id>', tracker, name='tracker'),
    path('productview/<slug:product_id>/', productview, name='ProductView'),
    path('checkout/', checkout, name='Checkout'),
    path('order', MyOrder, name='MyOrder'),
]
