from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Article(models.Model):
	
	title = models.CharField(max_length= 35, verbose_name= 'titulo')
	body = RichTextField(verbose_name= 'Cuerpo del Articulo')
	fe = models.DateField(blank = False, verbose_name= 'Emision del Articulo', auto_now_add= True)
	class Meta:
		ordering= ["-id"]
		verbose_name_plural = "Articulos"	
	def __str__(self):
		return str(self.title)