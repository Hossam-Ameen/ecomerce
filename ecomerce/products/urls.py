from django.urls import path
from . import views
urlpatterns = [
    path('' , views.ListProducts.as_view()),
    path('create/' , views.CreateProduct.as_view()),
    path('<int:pk>/' , views.GetProduct.as_view()),
    path("update/<int:pk>/",views.UpdateProduct.as_view(),name="update_product"),
    path("delete/<int:pk>/",views.DeleteProduct.as_view(),name="delete_product")
]
