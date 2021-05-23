from django.contrib import admin
from .models import Categoria, Endereco, Servico, Imagem, Comment

admin.site.register(
    [Categoria, Endereco, Servico, Imagem, Comment])
