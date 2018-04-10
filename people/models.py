from django.db import models
from PIL import Image

# Create your models here.

class profile(models.Model):

	name = models.CharField(max_length= 20, verbose_name= 'Nombre')
	bio = models.TextField(verbose_name= 'Bio del profile')
	img = models.ImageField(upload_to='miembros_comunidad', max_length= 100, blank=True)
	class Meta:
		ordering= ["name"]
		verbose_name_plural = "Miembros de la comunidad"	
	def __str__(self):
		return str(self.name)



class grupos(models.Model):
	nm = models.CharField(max_length=30, verbose_name='Nombre del Grupo')
	bg = models.TextField(verbose_name='Biografia del Grupo')
	ig  = models.ImageField(upload_to='Grupos_Comunidad', max_length= 100, blank= True)
	class Meta:
		ordering = ["nm"]
		verbose_name_plural = "Grupos de la Comunidad"
	def __str__(self):
		return str(self.nm)



class santos(models.Model):
	nms = models.CharField(max_length= 40, verbose_name= 'Nombre del Santo')
	bsn = models.TextField(verbose_name='Biografia del Santo')
	imsan = models.ImageField(upload_to= 'Santos_Comunidad', max_length= 100, blank= True)
	class Meta:
		ordering = ["nms"]
		verbose_name_plural = "Santos de la Comunidad"
	def __str__(self):
		return str(self.nms)



class foar(models.Model):

	nombre = models.CharField(max_length= 20, verbose_name= 'Nombre')
	biog = models.TextField(verbose_name= 'bio de la persona')
	imgs = models.ImageField(upload_to='Familia_OAR', max_length=100, blank=True)
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Orden Agustinos Recoleto"
	def __str__(self):
		return str(self.nombre)