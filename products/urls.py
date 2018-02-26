from django.contrib import admin
from django.urls import re_path, include

from products import views

admin.autodiscover()

urlpatterns = [
    re_path(r'^product/(?P<product_id>\w+)/$', views.product, name='product')
]
