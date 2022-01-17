from posixpath import basename
from django.urls import path,include
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stocks/', views.StockViewSet,basename="stocks")

urlpatterns = [
    path('', include(router.urls)),
]
