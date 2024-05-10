from django.urls import path
from product.views import AllProductsView

urlpatterns = [
    path('allproducts/',AllProductsView.as_view(),name='all')
]
