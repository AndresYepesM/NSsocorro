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

class foar(models.Model):

	nombre = models.CharField(max_length= 20, verbose_name= 'Nombre')
	biog = models.TextField(verbose_name= 'bio de la persona')
	imgs = models.ImageField(upload_to='Familia_OAR', max_length=100, blank=True)
	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Orden Agustinos Recoleto"
	def __str__(self):
		return str(self.nombre)