from django import forms
from .models import Tarea

class TareaFrom (forms.ModelForm):
  class Meta:
    model = Tarea
    exclude = []

