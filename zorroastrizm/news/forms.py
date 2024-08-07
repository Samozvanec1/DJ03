from .models import News
from django.forms import ModelForm, DateTimeInput, Textarea, TextInput


class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'short_desc', 'content', 'pub_date', 'user']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название новости'}),
            'short_desc': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'content': Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Содержание новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Дата публикации'}),
            'user': TextInput(attrs={'class': 'form-control', 'placeholder': 'Пользователь'})
        }
