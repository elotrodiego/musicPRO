from django.urls import path
from django.urls.resolvers import URLPattern
from django.conf.urls.static import static
from django.conf import settings

from .views import add_game, edit_game, delete_game, index, contacto, loginpage, registerpage, gamepage, logoutpage, paneladmin

urlpatterns = [
    path('', index, name='index'),
    path('contacto', contacto, name='contacto'),
    path('logoutpage', logoutpage, name='logout'),
    path('loginpage', loginpage, name='login'),
    path('registerpage', registerpage, name='registro'),
    path('gamepage/<pk>/', gamepage, name='gamepage'),
    path('paneladmin', paneladmin, name='paneladmin'),
    path('add_game', add_game, name='add_game'),
    path('edit_game/<pk>/', edit_game, name='edit_game'),
    path('delete_game/<pk>/', delete_game, name='delete_game'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)