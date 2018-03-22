from django.contrib import admin
from django.urls import re_path, include

from products import views

admin.autodiscover()

urlpatterns = [
    re_path(r'^product/(?P<product_id>\w+)/$', views.show_product, name='product'),
    re_path(r'^product/(?P<product_id>\w+)/comment/add$', views.add_comment, name='add_comment'),
]
