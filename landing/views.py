from django.shortcuts import render, render_to_response, redirect
from landing.forms import SubscriberForm

# Create your views here.
from products.models import ProductImage


def landing(request):
    name = 'Meow'
    form = SubscriberForm(request.POST or None)

    if request.POST and form.is_valid():
        form.save()
        return render(request, 'landing/landing.html', locals())
    return render(request, 'landing/landing.html', locals())


def home(request):
    products_images_jewsharps = ProductImage.objects.filter(is_main=True, product__category__name='Варганы')
    products_images_didgeridoos = ProductImage.objects.filter(is_main=True, product__category__name='Диджериду')
    products_images_cajons = ProductImage.objects.filter(is_main=True, product__category__name='Кахоны')

    return render(request,'landing/home.html', locals())
