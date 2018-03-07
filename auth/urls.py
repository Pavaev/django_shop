from django.urls import re_path
from . import views

app_name = 'auth'

urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
]
