from django_model_mutations import mutations, mixins

from apps.products import models, serializers
from apps.products.types import *


class ProductCreateMutation(mixins.LoginRequiredMutationMixin, mutations.CreateModelMutation):
    class Meta:
        serializer_class = serializers.ProductSerializer


class ProductUpdateMutation(mixins.LoginRequiredMutationMixin, mutations.UpdateModelMutation):
    class Meta:
        serializer_class = serializers.ProductSerializer


class ProductDeleteMutation(mixins.LoginRequiredMutationMixin, mutations.DeleteModelMutation):
    class Meta:
        model = models.Product

