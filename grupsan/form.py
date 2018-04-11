from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import grupos, santos
from PIL import ImageFilter


class Add_grupos(forms.ModelForm):
  class Meta:
    model = grupos
    fields = ('nm', 'bg', 'ig',)