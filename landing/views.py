from django.shortcuts import render, render_to_response, redirect
from landing.forms import SubscriberForm


# Create your views here.

def landing(request):
    name = 'Meow'
    form = SubscriberForm(request.POST or None)

    if request.POST and form.is_valid():
        form.save()
        return render(request, 'landing/landing.html', locals())
    return
