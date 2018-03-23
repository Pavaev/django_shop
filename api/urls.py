from django.contrib import admin
from django.urls import re_path, include

from api import views

admin.autodiscover()

urlpatterns = [
    re_path(r'^products/$', views.product_list, name='product_list'),
    re_path(r'^product/(?P<pk>\w+)/$', views.product_detail, name='product_detail')

]
