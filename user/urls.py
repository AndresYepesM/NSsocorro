from django.conf.urls import url
from django.contrib.auth import views as auth_views
from user import views

urlpatterns = [
	
	# Pagina para Ingresar a la plataforma.
	url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'}, name= 'login'),

	# Pagina del Logout.
	url(r'^logout/', auth_views.logout, name= 'logout'),

	# Pagina del Administrador.
	url(r'^adminsite/$', views.Ahome, name= 'home_logeado'),

	# Pagina de noticias.
	url(r'^noticias/$', views.notice, name= 'admin_noticias'),

	# Mensaje de Crear usuario correctamente
	url(r'^new_helper/$', views.registernew, name= 'new_helper'),

	# Formulario para registrar nuevos ayudantes.
	url(r'^register/', views.register, name= 'register')

]