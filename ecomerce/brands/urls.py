from django.urls import path
from . import views

urlpatterns = [
    path('' , views.ListBrands.as_view()),
    path('create/' , views.CreateBrand.as_view()),
    path('<int:pk>/' , views.GetBrand.as_view()),
    path("update/<int:pk>/",views.UpdateBrand.as_view(),name="update_brand"),
    path("delete/<int:pk>/",views.DeleteBrand.as_view(),name="delete_brand")
]
