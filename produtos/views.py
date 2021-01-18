from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Produto_2

from .forms import ProdutoForm

from django.contrib import messages

# Create your views here.
@login_required
def listaProdutos(request):

    search = request.GET.get('search')

    if search:

        produtos = Produto_2.objects.filter(nome__icontains=search)

        return render(request, 'produtos/listaProdutos.html', {'produtos':produtos})

    else:

        lista_produtos = Produto_2.objects.all().order_by('-created_at')

        paginator = Paginator(lista_produtos, 8)

        page = request.GET.get('page')

        produtos = paginator.get_page(page)

        return render(request, 'produtos/listaProdutos.html', {'produtos':produtos})

@login_required
def verProduto(request, id):

    produto = get_object_or_404(Produto_2, pk=id)

    return render(request, 'produtos/verProduto.html', {'produto':produto})

@login_required
def novoProduto(request):

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')


    else:
        form = ProdutoForm()
        return render(request, 'produtos/novoProduto.html', {'form':form})

@login_required
def editarProduto(request, id):

    produto = get_object_or_404(Produto_2, pk=id)
    form = ProdutoForm(instance=produto)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)

        if form.is_valid():
            produto.save()
            return redirect('/')
        else:
            return render(request, 'produtos/editarProduto.html', {'form':form, 'produto':produto})

    else:
        return render(request, 'produtos/editarProduto.html', {'form':form, 'produto':produto})

@login_required
def deletarProduto(request, id):
    produto = get_object_or_404(Produto_2, pk=id)
    produto.delete()

    messages.info(request, 'Tarefa Deletada Com Sucesso!')

    return redirect('/')