from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Collection, Product, Category, ProductImage, Contact


class ProductImageStackedInline(admin.StackedInline):
    model = ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'category', 'price', 'published', 'recommend']
    list_filter = ['published','category']
    search_fields = ['code', 'name', 'artist']
    inlines = [ ProductImageStackedInline ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'published']
    list_filter = ['published']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['Email','update']
    list_filter = ['update']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact,ContactAdmin)
