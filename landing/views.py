from django.shortcuts import render, render_to_response


# Create your views here.

def landing(request):
    name = 'Meow'
    return render(request, 'landing/landing.html', locals())