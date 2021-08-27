from django import forms
from .models import Drama

class dramaForm(forms.ModelForm):
    class Meta:
        model = Drama
        fields = ['title','writer', 'score', 'content', 'img']