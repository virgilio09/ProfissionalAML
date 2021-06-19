from django import forms
from .models import Comment

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