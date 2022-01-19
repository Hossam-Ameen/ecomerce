<<<<<<< HEAD
from posixpath import basename
from django.urls import path,include
=======
>>>>>>> main
from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename="products")
urlpatterns = router.urls
