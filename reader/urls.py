from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

	#Pagina de Inicio.
	url(r'^$', views.inicio, name= 'pagina_inicio'),

	# Pagina de articulos.
	url(r'^articulos/$', views.article_reader, name='article_reader'),

	# Pagina de Actividades.
	url(r'^actividades/$', views.activity_reader, name= 'activity_reader'),

	# Pagina de Miembros
	url(r'^miembros/$', views.people_reader, name= 'people_reader'),

	# PAgina de la Familia OAR
	url(r'^Familia_oar/$', views.foar_reader, name= 'foar_reader'),

	# Pagina para Grupos de la Comunidad
	url(r'^Grupos_Comunidad', views.grupos_reader, name='grupos_reader'),

	# Pagina de Santos
	url(r'^Santos_Comunidad', views.santos_reader, name='santos_reader')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)