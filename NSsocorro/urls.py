from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # App Para los Administradore's(Usuarios)
    url(r'^', include('user.urls')),

    # App para los Lectores
    url(r'^', include('reader.urls')),

    # App para Agrear Articulos.
    url(r'^', include('post_article.urls')),

    # App Para Agregar Actividades.
    url(r'^', include('post_activity.urls')),

    # App para Familia OAR, Miembros de la Comunidad
    url(r'^', include('people.urls')),

    # App Para Grupos y Santos
    url(r'^', include('grupsan.urls')),

    # CKEDITOR Editor de Documentos Online.
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
