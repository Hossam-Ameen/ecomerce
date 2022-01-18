from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'stocks', views.StockViewSet, basename="stocks")
urlpatterns = router.urls
