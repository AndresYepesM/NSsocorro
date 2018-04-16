from django.shortcuts import render, redirect
from django.template import loader
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from post_article.models import Article
from post_activity.models import Activity
from people.models import profile, foar
from grupsan.models import grupos, santos
from PIL import ImageFilter

# Create your views here.

def inicio(request):
	
	return render(request, 'lectores/inicio.html')

def article_reader(request):

	context = {'posts': Article.objects.all().order_by('-id')}
	return render(request, 'lectores/article_reader.html', context)

def activity_reader(request):

	context = {'posts': Activity.objects.all().order_by('-id')}
	return render(request, 'lectores/activity_reader.html', context)

def people_reader(request):

	context = {'posts': profile.objects.all().order_by('-id')}
	return render(request, 'lectores/people_reader.html', context)

def foar_reader(request):

	context = {'foar': foar.objects.all().order_by('-id')}
	return render(request, 'lectores/foar_reader.html', context)

def grupos_reader(request):

  context = {'grup': grupos.objects.all().order_by('-id')}
  return render(request, 'lectores/grupos_reader.html', context)

def santos_reader(request):

	context = {'sants': santos.objects.all().order_by('-id')}
	return render(request, 'lectores/santos_reader.html', context)