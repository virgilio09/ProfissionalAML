from django import forms
from django.contrib.auth import models
from django.forms import fields, widgets
from .models import Servico, Endereco, Comment

class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['nome', 'categoria', 'email', 'telefone01', 'telefone02', 'descricao']

        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome do servico'
            }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'Descreva seu serviço...',
                'rows': '3'
            }),
        }



class EndForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'bairro', 'estado', 'cidade']

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
