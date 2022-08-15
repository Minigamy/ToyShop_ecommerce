from django.urls import path

from store.authorization.authorization import LoginUser, logout_user, RegisterUser
from store.views import Home, ProductsByCategory, GetProduct, ProductsByBrand

app_name = 'store'

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('category/<slug:slug>/', ProductsByCategory.as_view(), name='category'),
    path('product/<slug:slug>/', GetProduct.as_view(), name='product'),
    path('brand/<slug:slug>/', ProductsByBrand.as_view(), name='brand'),

    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]
