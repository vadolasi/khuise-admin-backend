from django.urls import path

from apps.products import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='products-list'),
    path(
        '<int:pk>', views.ProductDetailView.as_view(),
        name='product-detail',
    ),
    path('add', views.ProductCreateView.as_view(), name='product-create'),
    path(
        '<int:pk>/update',
        views.ProductUpdateView.as_view(), name='product-update',
    ),
    path(
        '<int:pk>/delete',
        views.ProductDeleteView.as_view(), name='product-delete',
    ),
]
