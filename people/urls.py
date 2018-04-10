from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	

	#################################3 Miembros de la Comunidad ######################################3

	# Menu de los miembros de la iglesia.
	url(r'^listado_miembros/$', views.menbers_list, name= 'listado_miembros'),

	# Crear Nuevo Miembro
	url(r'^new_miembro/$', views.new_menbers , name= 'new_miembro'), 

	# Mensaje de Exito
	url(r'nuevo_miembro/$', views.people_mensaje, name= 'mensaje_miembro'),

	# Editar Miembros
	url(r'^(?P<id>\d+)/people_edit$', views.edit_menbers, name = 'edit_people'),

	# Borrar miembros.
	url(r'^(?P<id>\d+)/people_delete$', views.delete_menbers, name = 'delete_people'),


	################################# Orden Agustina Recoletos ######################################

	# Menu de la familia OAR.
	url(r'^listado_foar/$', views.foar_list, name= 'listado_foar'),

	# Crear nuevo Miembro de la Familia oar
	url(r'^nuevo_foar/$', views.new_foar, name= 'new_foar'),

	# Editar Miembros OAR
	url(r'^(?P<id>\d+)/foar_edit$', views.edit_foar, name = 'edit_foar'),

	# Borrar miembros OAR
	url(r'^(?P<id>\d+)/foar_delete$', views.delete_foar, name = 'delete_foar'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
