from posixpath import basename
from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'modules/', views.ModuleViewSet, basename="modules")

urlpatterns = [
    path('', include(router.urls)),
]
