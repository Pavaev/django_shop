from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import urls as rest_urls
from api.views import WorkWithProductSet, Login, WorkWithUserSet

router = DefaultRouter()
router.register('products', WorkWithProductSet)
router.register('users', WorkWithUserSet)
urlpatterns = router.get_urls()
urlpatterns += path('auth/login', Login.as_view()),
