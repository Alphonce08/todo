# apis/urls.py
from django.urls import path

from .views import TodoviewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', TodoviewSet, basename='todos')
urlpatterns = router.urls