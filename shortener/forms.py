from django.forms import ModelForm, TextInput
from .models import URL


class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ('long_url',)
        widgets = {
            'long_url': TextInput(attrs={
                'id': 'long_url',
                'placeholder': 'https://en.wikipedia.org/wiki/The_Triumph_of_Cleopatra',
                'autocomplete': 'off'
            })
        }
