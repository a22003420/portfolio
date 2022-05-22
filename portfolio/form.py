from django import forms
from django.forms import ModelForm
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control mb-2'
            }),
            'slug': forms.HiddenInput(attrs={
                'class': 'form-control'
            }),
            'autor': forms.Select(attrs={
                'class': 'form-select mb-2'
            }),
            'descricao': forms.Textarea(attrs={
                'class': 'form-control mb-2',
                'style': 'width: 100vh; height: 30%'
            }),
            'imagem': forms.FileInput(attrs={
                'class': 'form-control mb-2'
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'titulo': 'Título:',
            'descricao': 'Texto:'
        }