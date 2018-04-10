from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Article

class Add_Article(forms.ModelForm):

	body= forms.CharField(widget=CKEditorWidget())
	
	class Meta:
		model = Article
		fields = ('title', 'body',)