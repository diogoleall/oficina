from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import ServicoForm,OrdemServicoForm


from .models import Servico ,OrdemServico

from geral.models import Oficina

@login_required
def lista_servico(request):
    template_name = 'servicos/lista_servico.html'
    oficina = get_object_or_404(Oficina, usuario=request.user)
    servicos = Servico.objects.filter(oficina=oficina)
    context = {
        'servicos': servicos,
    }
    return render(request, template_name, context)


@login_required
def novo_servico(request):
    template_name = 'geral/novo_servico.html'
    context = {}
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
           of = form.save(commit=False)
           of.usuario = request.user
           of.save()
           messages.success(request, 'Serviço cadastrada com suscesso.')
           return redirect('geral:lista_servicos')
    form = ServicoForm()
    context['form'] = form
    return render(request, template_name, context)




@login_required
def editar_servico(request, pk):
    template_name = 'geral/novo_servico.html'
    context = {}
    Oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço editado com sucesso.')
            return redirect('geral:lista_servico')
    form = ServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def criar_ordem_servico(request, pk):
    template_name = 'servicos/criar_ordem_servico.html'
    context = {}
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ordem de Serviço criado com sucesso.')
            return redirect('servicos:lista_ordem_servico')
        
    form = OrdemServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def lista_ordem_servico(request):
    template_name = 'servicos/lista_ordem_servico.html'
    Oficina =get_object_or_404(Oficina, usuario=request.user)
    ordens_servicos = OrdemServico.objects.filter(Oficina=Oficina)
    context = {
        'ordens_servicos':ordens_servicos,
    }
    return render(request, template_name, context)