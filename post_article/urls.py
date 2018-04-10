from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

  # URLS DE CREACION DE ARTICULOS

	# PARA CREAR ARTICULOS.
	url(r'^new_article/$', views.createArticle, name= 'new_article'),

	# MENSAJE DE EXITO.
	url(r'^articulo_publicado/$', views.newArticle, name= 'articulo_publicado'),

	# LISTADO DE ARTICULOS.
	url(r'^listado_articulos/$', views.articleList, name= 'listado_admin'),

	# PARA EDITAR ARTICULOS.
	url(r'^(?P<id>\d+)/article_edit$', views.editArticle, name = 'edit_article'),

	# PARA BORRAR ARTICULOS.
	url(r'^(?P<id>\d+)/article_deleteArticle$', views.deleteArticle, name = 'delete_article'),
]