from django.http import request
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Categoria, Servico, Imagem, Comment
from .forms import CommentForm, ServicoForm, EndForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

def home(request):
    categorias = Categoria.objects.all()
    qtd_servico = Servico.objects.count()
    qtd_user = User.objects.count()

    nome = request.GET.get('nome')
    estado = request.GET.get('estado')
    cidade = request.GET.get('cidade')
    category = request.GET.get('category')

    existe = True

    servicos_list = Servico.objects.all().order_by('-created_at')

    if(servicos_list.exists()): 
    
        # filter
        if nome and estado and cidade and category:
            servicos_list = Servico.objects.select_related('endereco').filter(nome__icontains=nome, endereco__estado=estado, endereco__cidade=cidade, categoria=category)

        elif estado and cidade and category:
            servicos_list = Servico.objects.select_related('endereco').filter(endereco__estado=estado, endereco__cidade=cidade, categoria=category)
        
        elif estado and cidade:
            servicos_list = Servico.objects.select_related('endereco').filter(endereco__estado=estado, endereco__cidade=cidade)
        
        elif nome:
            servicos_list = Servico.objects.filter(nome__icontains=nome)

        paginator = Paginator(servicos_list, 1)

        page = request.GET.get('page')
        servicos = paginator.get_page(page)
    
    else:
        existe = False

    context = { 
        'servicos': servicos,
        'categorias': categorias,
        'qtd_user': qtd_user,
        'qtd_servico': qtd_servico,
        'existe': existe
    }
    
    return render(request, 'index.html', context)

def about(request):
    qtd_servicos = Servico.objects.count()
    qtd_user = User.objects.count()

    context = {
        'qtd_servicos': qtd_servicos,
        'qtd_user': qtd_user,
    }

    return render(request, 'servico/about.html', context)


def addServico(request):

    if request.method == 'POST': 
        servicoForm = ServicoForm(request.POST)
        endForm = EndForm(request.POST)   
        images = request.FILES.getlist('images')

        if servicoForm.is_valid() and endForm.is_valid():
            servico = servicoForm.save(commit=False)
            endereco = endForm.save(commit=False)
            endereco.save()

            servico.user = request.user
            servico.ativo = 'ativo'
            servico.endereco_id = endereco.id
            servico.capa = images.pop(0)
            servico.save()
         
            # upload das images
            if(images != []):
                for image in images:
                    photo = Imagem.objects.create(
                        servico_id=servico.id,
                        image=image,
                    )
            
            messages.success(request, 'Serviço adicionado com sucesso..')
            return redirect('dashboard')
       
    else:
        servicoForm = ServicoForm()
        endForm = EndForm()

        context = {
            'servicoForm': servicoForm,
            'endForm': endForm,
        
        }

        return render(request, 'servico/addservico.html', context)


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
        
            messages.success(request, 'Comentario adicionado com sucesso..')
            
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

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


def removeServico(request, id):
    servico = get_object_or_404(Servico, pk=id)
    servico.delete()

    messages.success(request, 'Serviço removido com sucesso..')
    
    return redirect('dashboard')


def dashboard(request):
    
    search = request.GET.get('search')
    filter = request.GET.get('filter')
    achou = False # caso encontre algo na busca
    exite = True # caso exita algum serviço 
    status = False # active or not 
    
    servicos = Servico.objects.all().order_by('-created_at').filter(user=request.user)

    if(servicos.exists()): 
        if search:
            servicos = Servico.objects.filter(nome__icontains=search, user=request.user)

            if(servicos.exists()):
                achou = True
        elif filter and filter != "todos":
            servicos = Servico.objects.filter(ativo=filter, user=request.user)

            if(servicos.exists()):
                status = True

    else:
        exite = False

    context = {
        'servicos': servicos,
        'achou': achou,
        'exite': exite,
        'status': status
        
    }

    return render(request, 'servico/dashboard.html', context)