from django.urls import re_path
from . import views

app_name = 'landing'

urlpatterns = [
    re_path(r'^$', views.landing, name='landing')
]
