from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Activity

class Add_Activity(forms.ModelForm):

	cuerpo = forms.CharField(widget=CKEditorWidget())
	
	class Meta:
		model = Activity
		fields = ('titulo', 'cuerpo',)

