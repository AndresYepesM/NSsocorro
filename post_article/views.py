from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from post_article.models import Article
from PIL import ImageFilter
from .form import *

# Create your views here.

# Para Crear articulos
@login_required(login_url= '/login/')
# LISTADO DE ARTICULOS.
def articleList(request):

	context = {'posts': Article.objects.all().order_by('-id')}
	return render(request, 'articulos/create_article_list.html', context)


@login_required(login_url='/login/')
# MENSAJE DE PUBLICACION.
def newArticle(request):

	return render(request, 'articulos/new_article.html')	


@login_required(login_url='/login/')
# METODO PARA CREAR ARTICULOS.
def createArticle(request):

	if request.method == 'POST':
		form = Add_Article(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('articulo_publicado'))
	else:
		form = Add_Article()

	context = {'form' : form}
	return render(request, 'articulos/add_article.html', context)


@login_required(login_url='/login/')
# METODO DE EDITAR ARTICULOS.
def editArticle(request, id):

	post = get_object_or_404(Article, id=id)
	if request.method == 'POST':
		form = Add_Article(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit= False)
			post.save()
			return redirect('listado_admin')
	else:
		form = Add_Article(instance=post)
	context = {'form' : form}
	return render(request, 'articulos/edit_article.html', context)

@login_required(login_url='/login/')
# METODO PARA BORRAR ARTICULOS.
def deleteArticle(request, id):
	post = get_object_or_404(Article, id=id)
	post.delete()
	return redirect('listado_admin')