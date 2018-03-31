from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views.decorators.http import require_POST

from authentication.forms import RegisterForm


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=my_password)
            login(request=request, user=user)
            return redirect(reverse('landing:home'))
    else:
        form = RegisterForm()
    return render(request, 'landing/register.html',
                  locals())


@require_POST
def sign_in(request):
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(email=email, password=password)
    if user is not None:
        login(request=request, user=user)
        return redirect(reverse('landing:home'))
    else:
        return redirect(reverse('landing:home'))


def log_out(request):
    logout(request)
    return redirect(reverse('landing:home'))