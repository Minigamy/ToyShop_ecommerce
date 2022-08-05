from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from store.models import Category, Product, Brand


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'



class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('id', 'title', 'slug', 'parent_category')
    list_display_links = ('id', 'title')
    search_fields = ('title', )


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    form = ProductAdminForm
    list_display = ('id', 'name', 'price', 'stock', 'available', 'brand', 'article', 'created', 'updated', 'get_image')
    list_filter = ('available', 'category', 'created', 'updated')
    list_editable = ('price', 'stock', 'available')
    list_display_links = ('name',)
    search_fields = ('name', )
    fields = ('name', 'slug', 'category', 'description', 'image', 'article', 'price', 'stock', 'available', 'manufacturer_country', 'brand', 'package_size', 'weight')

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="60">')
        return '-'

    get_image.short_description = 'Фото'


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug')
    list_display_links = ('title',)
    search_fields = ('title', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
