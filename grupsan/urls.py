from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

  ################################# Grupos ######################################

  # Menu de Grupos de la Comunidad
  url(r'^listado_grupos/$', views.grupos_list, name= 'listado_grupos'),

  # Mensjase
  url(r'nuevo_grupo/$', views.new_grupos, name= 'mensaje_grupo'),

  # Crear nuevo Miembro de la Familia oar
  url(r'^nuevo_grupos/$', views.add_grupos, name= 'new_grupos'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)