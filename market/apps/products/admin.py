from django.contrib import admin
from django.utils.html import format_html
from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]
    list_filter = ['category']

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductCategory._meta.fields]

    class Meta:
        model = ProductCategory


admin.site.register(ProductCategory, ProductCategoryAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="100" />'.format(obj.image.url))

    def save_model(self, request, obj, form, change):
        files = request.FILES.getlist('files')
        for f in files:
            instance = ProductImage(files=f)
            instance.save()

    image_tag.short_description = 'Image'
    list_display = list_display + ['image_tag']
    readonly_fields = ['image_tag']
    list_filter = ['product']

    class Meta:
        model = ProductImage


admin.site.register(ProductImage, ProductImageAdmin)
