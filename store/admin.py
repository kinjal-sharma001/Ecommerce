from django.contrib import admin
from .models import Product, ProductReview, Warehouse

# Register your models here.
class ProductReviewInline(admin.TabularInline):
    model = ProductReview
    extra = 0
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    inlines = [ProductReviewInline]

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    filter_horizontal = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(Warehouse, WarehouseAdmin)