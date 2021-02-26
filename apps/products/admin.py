from django.contrib import admin

from apps.products import models


# class ProductImageAdmin(admin.StackedInline):
#     model = models.Image


# class ProductStockAdmin(admin.StackedInline):
#     model = models.Stock


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    # inlines = [ProductImageAdmin, ProductStockAdmin]
    list_display = ['name', 'price']
    search_fields = ['name', 'price']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin): pass

