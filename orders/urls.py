from django.contrib import admin
from django.urls import re_path, include

from orders import views

admin.autodiscover()

urlpatterns = [
    re_path('^cart_addition/$', views.add_to_cart, name='add_to_cart'),
    # re_path('^checkout/$', views.checkout, name='checkout')

]
