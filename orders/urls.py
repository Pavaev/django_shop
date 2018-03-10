from django.contrib import admin
from django.urls import re_path, include

from orders import views

admin.autodiscover()

urlpatterns = [
    re_path('^basket_addition/$', views.add_to_basket, name='add_to_basket'),
    # re_path('^checkout/$', views.checkout, name='checkout')

]
