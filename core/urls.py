from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings

from .views import index, contacto, login, registro, gamepage

urlpatterns = [
    path('', index, name='index'),
    path('contacto', contacto, name='contacto'),
    path('login', login, name='login'),
    path('registro', registro, name='registro'),
    path('gamepage/<pk>', gamepage, name='gamepage')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)