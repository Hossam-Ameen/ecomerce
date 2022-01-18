from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'brands', views.BrandViewSet, basename="brands")
urlpatterns = router.urls
