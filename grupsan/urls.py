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

  # Editar Grupos de la Comunidad
  url(r'^(?P<id>\d+)/grupos_edit$', views.grupos_edit, name = 'edit_grupos'),

  # Borrar Grupos de la Comunidad
  url(r'^(?P<id>\d+)/grupos_delete$', views.delete_grupos, name = 'delete_grupos'),

  ################################# Santos ######################################

  # Menu de Santos de la Comunidad
  url(r'^listado_santos/$', views.santos_list, name= 'listado_santos'),

  # Mensjase
  url(r'nuevo_santos/$', views.new_santos, name= 'mensaje_santos'),

  # Crear nuevo Miembro de la Familia oar
  url(r'^nuevo_santos/$', views.add_santos, name= 'new_santos'),

  # Editar Grupos de la Comunidad
  url(r'^(?P<id>\d+)/santos_edit$', views.santos_edit, name = 'edit_santos'),

  # Borrar Grupos de la Comunidad
  url(r'^(?P<id>\d+)/santos_delete$', views.santos_delete, name = 'delete_santos'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)