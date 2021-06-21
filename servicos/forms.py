from django import forms
from django.contrib.auth import models
from .models import Servico, Imagem, Endereco, Comment

# class ServicoForm(forms. ModelForm):

#     class Meta:
#         model = 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['nome', 'comment']

        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Seu nome'
                
            }),
            'comment': forms.Textarea(attrs={
                'placeholder': 'Adicione um comentário...',
                'rows': '4'
            })
        }
