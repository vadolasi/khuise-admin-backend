from django.urls import path

from apps.products import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products-list'),
    path(
        'product/<int:id>', views.ProductDetailView.as_view(),
        name='product-detail',
    ),
    path('add-product/', views.ProductCreateView.as_view(), name='product-create'),
    path(
        'update-product/<int:id>',
        views.ProductUpdateView.as_view(), name='product-update',
    ),
    path(
        'delete-product/<int:id>',
        views.ProductDeleteView.as_view(), name='product-delete',
    ),
]
