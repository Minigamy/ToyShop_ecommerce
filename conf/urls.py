from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('', include('store.urls', namespace='store')),
]

""" Если устанговлен режим дебага True, то джанго будет брать медиа из папок которые мы указали. """
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
