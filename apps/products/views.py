from django.contrib.auth.decorators import login_required
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic

from apps.products import forms, models


@method_decorator(login_required, name='dispatch')
class ProductListView(generic.ListView):
    model = models.Product
    template_name = 'products/products_list.pug'
    context_object_name = 'products'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        products = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(products, self.paginate_by)

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)

        context['products'] = products

        return context


@method_decorator(login_required, name='dispatch')
class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = 'products/product_detail.pug'
    context_object_name = 'product'


class ProductCreateView(generic.CreateView):
    form_class = forms.ProdutoForm
    template_name = 'products/product_create.pug'

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'id': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(generic.UpdateView):
    model = models.Product
    template_name = 'products/product_update.pug'
    context_object_name = 'product'

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(generic.DeleteView):
    model = models.Product
    template_name = 'products/product_delete.pug'
    success_url = reverse_lazy('products-list')
