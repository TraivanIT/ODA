from django.shortcuts import render
from . models import *


#home page
def home(request):
    homes_sliders = HomeSliderText.objects.all()
    home_texts = Home.objects.all()
    context = {'home_texts': home_texts, 'homes_sliders': homes_sliders,}
    return render(request, 'pages/home.html', context)



def kidsdream(request):
    kids_sliders = KidsDreamTextSlider.objects.all()
    kids_texts = KidsDreamText.objects.all()
    context = {'kids_sliders': kids_sliders, 'kids_texts': kids_texts}
    return render(request, 'pages/kidsdream.html', context)


def wishlist(request):
    wish_list_sliders = WishListSliderText.objects.all()
    wish_list_texts = WishListText.objects.all()
    context = {'wish_list_sliders': wish_list_sliders, 'wish_list_texts': wish_list_texts}
    return render(request, 'pages/wishlist.html', context)


def donate(request):
    donate_texts = DonateText.objects.all()
    donate_sliders = DonateSliderText.objects.all()
    context = {'donate_texts': donate_texts, 'donate_sliders': donate_sliders}
    return render(request, 'pages/donate.html', context)


def contact(request):
    return render(request, 'pages/contact.html')


def getinvoled(request):
    return render(request, 'pages/getinvoled.html')


def aboutus(request):
    return render(request, 'pages/aboutus.html')
