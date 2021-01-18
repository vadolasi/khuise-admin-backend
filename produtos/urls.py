from django.urls import path
from . import views

urlpatterns = [
    path('', views.listaProdutos, name='lista-produtos'),
    path('produto/<int:id>', views.verProduto, name='ver-produto'),
    path('novoproduto/', views.novoProduto, name='novo-produto'),
    path('editarproduto/<int:id>', views.editarProduto, name='editar-produto'),
    path('deletarproduto/<int:id>', views.deletarProduto, name='deletar-produto')
]