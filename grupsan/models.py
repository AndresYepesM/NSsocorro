from django.db import models
from PIL import Image

# Create your models here.

class grupos(models.Model):

	nm = models.CharField(max_length= 20, verbose_name= 'Nombre del grupo')
	bg = models.TextField(verbose_name= 'Bio del grupo')
	ig = models.ImageField(upload_to='Grupos_comunidad', max_length= 100, blank=True)
	class Meta:
		ordering= ["nm"]
		verbose_name_plural = "Grupos de la comunidad"	
	def __str__(self):
		return str(self.nm)

class santos(models.Model):

	nms = models.CharField(max_length= 20, verbose_name= 'Nombre del santo')
	bgs = models.TextField(verbose_name= 'bio del santo')
	imgs = models.ImageField(upload_to='Santos_Comunidad', max_length=100, blank=True)
	class Meta:
		ordering = ["nms"]
		verbose_name_plural = "Santos de la Comunidad"
	def __str__(self):
		return str(self.nms)