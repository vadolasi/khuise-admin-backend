from django.contrib import admin

from apps.products import models


class ProductImageAdmin(admin.StackedInline):
    model = models.ProductImage

class ProductStockAdmin(admin.StackedInline):
    model = models.ProductStock


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin, ProductStockAdmin]
    list_display = ['name', 'price', 'categories']
    search_fields = ['name', 'price', 'categories']
