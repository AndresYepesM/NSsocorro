from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from PIL import ImageFilter
from .models import profile, foar
from .form import Add_miembro, Add_foar

# Create your views here.

########################################## Mienbros de la comunidad ########################################

@login_required(login_url= '/login/')
# LISTADO DE LOS MIEMBROS.
def menbers_list(request):

	context = {'posts': profile.objects.all().order_by('-id')}
	return render(request, 'people/miembros/list_people_menu.html', context)

@login_required(login_url= '/login/')
# MENSAJE
def people_mensaje(request):

	return render(request, 'people/miembros/new_people.html')	

@login_required(login_url= '/login/')
# AGREGAR MIEMBRO.
def new_menbers(request):

  if request.method == 'POST':
    form = Add_miembro(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('mensaje_miembro'))
  else:
    form = Add_miembro()

  context = {'form' : form}
  return render(request, 'people/miembros/add_people.html', context)

@login_required(login_url= '/login/')
# EDITAR MIEMBRO.
def edit_menbers(request, id):

  post = get_object_or_404(profile, id=id)
  if request.method == 'POST':
    form = Add_miembro(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save(commit= False)
      post.save()
      return redirect('listado_miembros')
  else:
    form = Add_miembro(instance=post)
  context = {'form' : form}
  return render(request, 'people/miembros/edit_people.html', context)

@login_required(login_url= '/login/')
# BORRAR MIEMBRO.
def delete_menbers(request, id):

  post = get_object_or_404(profile, id=id)
  post.delete()
  return redirect('listado_miembros')



############################################ FAMILIA OAR ################################################


@login_required(login_url= '/login/')
# LISTADO DE LA FAMILIA OAR
def foar_list(request):

  context = {'foar': foar.objects.all().order_by('-id')}
  return render(request, 'people/foar/list_foar_menu.html', context)


@login_required(login_url= '/login/')
# Agregar FOAR
def new_foar(request):

  if request.method == 'POST':
    form = Add_foar(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(reverse('mensaje_miembro'))
  else:
    form = Add_foar()

  context = {'form' : form}
  return render(request, 'people/foar/add_foar.html', context)

@login_required(login_url= '/login/')
# EDITAR MIEMBRO.
def edit_foar(request, id):

  post = get_object_or_404(foar, id=id)
  if request.method == 'POST':
    form = Add_foar(request.POST, request.FILES, instance=post)
    if form.is_valid():
      post = form.save(commit= False)
      post.save()
      return redirect('listado_miembros')
  else:
    form = Add_foar(instance=post)
  context = {'form' : form}
  return render(request, 'people/foar/edit_foar.html', context)

@login_required(login_url= '/login/')
# BORRAR MIEMBRO.
def delete_foar(request, id):

  post = get_object_or_404(foar, id=id)
  post.delete()
  return redirect('listado_foar')