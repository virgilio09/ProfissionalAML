from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Categoria, Servico, Imagem, Comment
from .forms import CommentForm


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
    # Objects 
    servico = get_object_or_404(Servico, pk=id)
    comments = Comment.objects.filter(servico_id=id)
    qtd_comments = len(comments)
    images = Imagem.objects.filter(servico_id=id)

    # Commet form 
    if request.method == 'POST': 
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            comment = commentForm.save(commit=False)
            comment.servico_id = id
            comment.save()
            # return redirect('home')

    else:
        commentForm = CommentForm()

        context = {
            'servico': servico, 
            'comments': comments, 
            'qtd_comments': qtd_comments, 
            'images': images,
            'commentForm': commentForm
        }

        return render(request, 'servico/servicoView.html', context)