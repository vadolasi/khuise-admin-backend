from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name="products-list"),
    path("produto/<int:id>", views.ProductDetailView.as_view(), name="product-detail"),
    path("novoproduto/", views.ProductCreateView.as_view(), name="product-create"),
    path("editarproduto/<int:id>", views.ProductUpdateView.as_view(), name="product-update"),
    path("deletarproduto/<int:id>", views.ProductDeleteView.as_view(), name="product-delete")
]
