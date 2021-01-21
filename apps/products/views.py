from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import generic
from django_filters.views import FilterView
from django.db import transaction

from apps.products import forms, models, filters


@method_decorator(login_required, name='dispatch')
class ProductListView(FilterView):
    model = models.Product
    template_name = 'products/products_list.pug'
    context_object_name = 'products'
    paginate_by = 15
    filterset_class = filters.ProductFilter


@method_decorator(login_required, name='dispatch')
class ProductDetailView(generic.DetailView):
    model = models.Product
    template_name = 'products/product_detail.pug'
    context_object_name = 'product'


@method_decorator(login_required, name='dispatch')
class ProductCreateView(generic.CreateView):
    form_class = forms.ProductForm
    template_name = 'products/product_create.pug'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            data['images_form'] = forms.imagesFormSet(self.request.POST)
            data['stock_form'] = forms.stockFormSet(self.request.POST)
        else:
            data['images_form'] = forms.imagesFormSet()
            data['stock_form'] = forms.stockFormSet()

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['images_form']
        stock_form = context['stock_form']
        self.object = form.save()

        with transaction.atomic():
            form.instance.created_by = self.request.user
            if image_form.is_valid() and stock_form.is_valid():
                image_form.instance = self.object
                stock_form.instance = self.object
                image_form.save()
                stock_form.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProductUpdateView(generic.UpdateView):
    model = models.Product
    form_class = forms.ProductForm
    template_name = 'products/product_update.pug'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        if self.request.POST:
            data['images_form'] = forms.imagesFormSet(self.request.POST, instance=self.object)
            data['stock_form'] = forms.stockFormSet(self.request.POST, instance=self.object)
        else:
            data['images_form'] = forms.imagesFormSet(instance=self.object)
            data['stock_form'] = forms.stockFormSet(instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        image_form = context['images_form']
        stock_form = context['stock_form']
        self.object = form.save()

        with transaction.atomic():
            form.instance.created_by = self.request.user
            if image_form.is_valid() and stock_form.is_valid():
                image_form.instance = self.object
                stock_form.instance = self.object
                image_form.save()
                stock_form.save()


        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product-detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class ProductDeleteView(generic.DeleteView):
    model = models.Product
    template_name = 'products/product_delete.pug'
    success_url = reverse_lazy('products-list')
