from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.BrandViewSet, basename='brands')

urlpatterns = [
    path('', include(router.urls)),
]