from django import forms

from .models import Contactenos

class PostForm(forms.ModelForm):

    class Meta:
        model = Contactenos
        fields = ('correo', 'mensaje',)