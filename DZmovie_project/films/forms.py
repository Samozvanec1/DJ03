from .models import Film
from django.forms import ModelForm,  Textarea, TextInput


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = ['name', 'Like', 'spoiler']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Как звать'}),
            'spoiler': Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Расскажи о чём (спойлеруй!)'}),
            'Like': TextInput(attrs={'class': 'form-control', 'placeholder': 'Отношение (+ или -)'}),
        }