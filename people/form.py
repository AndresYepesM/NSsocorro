from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import profile, foar
from PIL import ImageFilter

class Add_miembro(forms.ModelForm):
	class Meta:
		model = profile
		fields = ('name', 'bio', 'img',)


class Add_foar(forms.ModelForm):
	class Meta:
			model = foar
			fields = ('nombre', 'biog', 'imgs',)
