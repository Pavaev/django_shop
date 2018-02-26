from django.contrib import admin
from django.urls import re_path, include

from orders import views

admin.autodiscover()

urlpatterns = [
    re_path('^basket_addition/$', views.basket_addition, name='basket_addition')
]
