from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from PIL import ImageFilter
from .models import Activity
from .form import *

# Create your views here.

@login_required(login_url= '/login/')
# LISTADO DE LAS ACTIVIDADES.
def activityList(request):

	context = {'posts': Activity.objects.all().order_by('-id')}
	return render(request, 'actividades/create_activity_list.html', context)

@login_required(login_url= '/login/')
# MENSAJE DE EXITO AL PUBLICAR LAS ACTIVIDADES
def NewActivity(request):

	return render(request, 'actividades/new_activity.html')


@login_required(login_url= '/login/')
# CREAR ACTIVIDADES.
def createActivity(request):

	if request.method == 'POST':
		form = Add_Activity(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('actividad_publicada'))
	else:
		form = Add_Activity()

	context = {'form' : form}
	return render(request, 'actividades/add_activity.html', context)

@login_required(login_url= '/login/')
# EDITAR ACTIVIDADES.
def editArticle(request, id):

	post = get_object_or_404(Activity, id=id)
	if request.method == 'POST':
		form = Add_Activity(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit= False)
			post.save()
			return redirect('listado_actividades')
	else:
		form = Add_Activity(instance=post)
	context = {'form' : form}
	return render(request, 'actividades/edit_activity.html', context)

@login_required(login_url='/login/')
# METODO PARA BORRAR ACTIVIDADES.
def deleteActivity(request, id):
	post = get_object_or_404(Activity, id=id)
	post.delete()
	return redirect('listado_actividades')