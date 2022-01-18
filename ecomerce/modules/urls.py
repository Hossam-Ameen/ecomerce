from . import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'modules', views.ModuleViewSet, basename="modules")
urlpatterns = router.urls
