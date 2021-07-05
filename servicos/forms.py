from django import forms
from django.contrib.auth import models
from django.forms import fields, widgets
from .models import Servico, Endereco, Comment
from django.core.exceptions import ValidationError


class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = ['status','nome', 'categoria', 'email', 'telefone01', 'telefone02', 'descricao']

        widgets = {

            'descricao': forms.Textarea(attrs={
                'placeholder': 'Descreva seu serviço...',
                'rows': '4'
            }),
            'telefone01': forms.TextInput(attrs={
                'class':'sp_celphones'
            }),
            'telefone02': forms.TextInput(attrs={
                'class':'sp_celphones'
            }),
            
        }

class EndForm(forms.ModelForm):

    class Meta:
        model = Endereco
        fields = ['cep', 'rua', 'numero', 'complemento', 'bairro', 'estado', 'cidade']

        widgets = {
            'cep': forms.TextInput(attrs={'class': 'cep', 'id': 'cep'}),
            'rua': forms.TextInput(attrs={'id': 'rua'}),
            'bairro': forms.TextInput(attrs={'id': 'bairro'}),
            'estado': forms.TextInput(attrs={'id': 'uf'}),
            'cidade': forms.TextInput(attrs={'id': 'cidade'}),
        }

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
    