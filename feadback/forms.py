from django import forms
from .models import Feadback

class feadbackform(forms.ModelForm):
    class Meta:
        model:Feadback
        fields=['__all__']
        