from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .form import *

# Create your views here.

#  Metodo para Entrar en la Pagina de Administrador.
@login_required(login_url='/login/')
def Ahome(request):

	return render(request, 'user/home_logeado.html')

@login_required(login_url='/login/')
def registernew(request):

	return render(request, 'user/register_new.html')	

# Metodo para Registrar nuevos ayudantes.
@login_required(login_url='/login/')
def register(request):

	if request.method == 'POST':
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			userObj = form.cleaned_data
			username = userObj['username']
			email = userObj['email']
			password = userObj['password']
			if not(User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
				User.objects.create_user(username, email, password)
				user = authenticate(username=username, password=password)
				return HttpResponseRedirect('/new_helper')
			else:
				raise form.ValidationError('Ya Existe un Usuario Con estos Datos')
	else:
		
		form = UserRegistrationForm()

	return render(request, 'user/singup.html', {'form' : form })	

# Pagina de noticias.
@login_required(login_url='/login/')
def notice(request):

	return render(request, 'user/notice.html')


	

	
