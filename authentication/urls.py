from django.urls import re_path
from . import views

app_name = 'auth'

urlpatterns = [
    re_path(r'^register/$', views.sign_up, name='register'),
    re_path(r'^login/$', views.sign_in, name='login'),
    re_path(r'^logout/$', views.log_out, name='logout'),
    re_path(r'^verify/(?P<uuid>[a-z0-9\-]+)/', views.verify, name='verify')
]
