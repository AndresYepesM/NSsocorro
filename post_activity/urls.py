from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [

	# Listado de Actividades.
	url(r'^listado_actividades/$', views.activityList, name= 'listado_actividades'),

	# Crear Actividades.
	url(r'^new_activity/$', views.createActivity, name= 'nueva_actividad'),

	# Mensaje de Exito al crear la Actividad.
	url(r'^actividad_publicada/$', views.NewActivity, name= 'actividad_publicada'),

	# Editar las Actividades.
	url(r'^(?P<id>\d+)/activity_edit$', views.editArticle, name = 'edit_activity'),

	# Borrar Actividades
	url(r'^(?P<id>\d+)/activity_delete$', views.deleteActivity, name = 'delete_activity'),
]
