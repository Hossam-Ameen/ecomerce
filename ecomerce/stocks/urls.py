from . import views
from django.urls import path
urlpatterns = [
    path('' , views.ListStocks.as_view()),
    path('create/' , views.CreateStock.as_view()),
    path('<int:pk>/' , views.GetStock.as_view()),
    path("update/<int:pk>/",views.UpdateStock.as_view(),name="update_stock"),
    path("delete/<int:pk>/",views.DeleteStock.as_view(),name="delete_stock")
]
