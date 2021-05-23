from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Categoria, Servico, Imagem


def home(request):
    categorias = Categoria.objects.all()
    servicos = Servico.objects.all()
    qtd_user = User.objects.count()
    

    context = { 'servicos': servicos,
                'categorias': categorias,
                'qtd_user': qtd_user
    }
    
    return render(request, 'index.html', context)

def addServico(request):

    return render(request, 'servico/addservico.html')


def servicoView(request, id):
    servico = get_object_or_404(Servico, pk=id)
    # image = Imagem.objects.get(pk=id)
    # images = servico.image_set.all()   

    context = {'servico': servico}
    return render(request, 'servico/servicoView.html',context)