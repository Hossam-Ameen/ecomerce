from django.urls.conf import path
from . import views 


urlpatterns = [
    path('' , views.ListModules.as_view()),
    path('create/' , views.CreateModule.as_view()),
    path('<int:pk>/' , views.GetModule.as_view()),
    path("update/<int:pk>/",views.UpdateModule.as_view(),name="update_Module"),
    path("delete/<int:pk>/",views.DeleteModule.as_view(),name="delete_Module")
]
