#São as importações realizadas de forma a utilizar partes do Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

#Lista responsável por organizar as urls do sistema
urlpatterns = [
    path('', include('sistema.urls')),
    path('admin/', admin.site.urls),

    
]

#path() -> é um método do Django que permite realizar a inserção de uma uma URL

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)