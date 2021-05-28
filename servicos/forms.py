from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['nome', 'comment']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Seu nome'
                
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Adicione um comentário...',
                'rows': '3'
            })
        }