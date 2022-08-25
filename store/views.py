from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from cart.forms import CartAddProductForm
from store.models import Category, Product, Brand

from .recommender import Recommender


class Home(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Интернет магазин игрушек'
        return context


class ProductsByCategory(ListView):
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 4

    # allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        context['prod_cat'] = Category.objects.filter(parent_category__slug=self.kwargs['slug'])
        return context


class ProductsByBrand(ListView):
    template_name = 'store/index.html'
    context_object_name = 'products'
    paginate_by = 4

    # allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(brand__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Brand.objects.get(slug=self.kwargs['slug'])
        return context


class GetProduct(DetailView):
    model = Product
    template_name = 'store/single.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CartAddProductForm()
        r = Recommender()
        slug = self.request.get_full_path().replace('/product/', '').replace('/', '')
        product = get_object_or_404(Product,slug=slug)
        context['recommended_products'] = r.suggest_products_for([product], 4)
        return context
