from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('kidsdream', views.kidsdream, name='kidsdream'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('donate', views.donate, name='donate'),
    path('contact', views.contact, name='contact'),
    path('getinvoled', views.getinvoled, name='getinvoled'),
    path('aboutus', views.aboutus, name='aboutus'),

]
