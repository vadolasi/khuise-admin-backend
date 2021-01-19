from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from .models import Produto

from .forms import ProdutoForm

from django.contrib import messages


@method_decorator(login_required, name="dispatch")
class ProductListView(ListView):
    model = Produto
    template_name = "produtos/listaProdutos.html"
    context_object_name = "produtos"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = self.get_queryset()
        page = self.request.GET.get("page")
        paginator = Paginator(products, self.paginate_by)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context["products"] = products

        return context


@method_decorator(login_required, name="dispatch")
class ProductDetailView(DetailView):
    model = Produto
    template_name = "produtos/verProduto.html"
    context_object_name = "produto"


class ProductCreateView(CreateView):
    form_class = ProdutoForm
    template_name = "produtos/novoProduto.html"

    def get_success_url(self):
        return reverse_lazy("product-detail", kwargs={"id": self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(UpdateView):
    model = Produto
    template_name = "produtos/editarProduto.html"
    context_object_name = "produto"

    def get_success_url(self):
        return reverse_lazy("product-detail", kwargs={"pk": self.object.pk})


@method_decorator(login_required, name="dispatch")
class ProductDeleteView(DeleteView):
    model = Produto
    template_name = "produtos/product_delete.html"
    success_url = reverse_lazy("products-list")
