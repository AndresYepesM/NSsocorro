from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Activity(models.Model):
	
	titulo = models.CharField(max_length= 32, verbose_name= 'Titulo de la Actividad')
	cuerpo = RichTextField(verbose_name= 'Cuerpo del Articulo')
	fp= models.DateField(blank = False, verbose_name= 'Fecha de Publicacion', auto_now_add= True)
	class Meta:
		ordering= ["-id"]
		verbose_name_plural = "Actividades"	
	def __str__(self):
		return str(self.titulo)