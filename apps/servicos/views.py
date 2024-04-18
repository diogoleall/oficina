from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

from .forms import ServicoForm

from .models import Servico
from geral.models import Oficina

@login_required
def lista_servico(request):
    template_name = 'servicos/lista_servico.html'
    Oficina =get_object_or_404(Oficina, usuario=request.user)
    servicos = Servico.objects.filter(Oficina=Oficina)
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
def excluir_servico(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    servico.delete()
    messages.info(request, 'Serviço excluído com sucesso.')
    return redirect('geral:lista_servico')

@login_required
def editar_servico(request, pk):
    template_name = 'geral/novo_servico.html'
    context = {}
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço editado com sucesso.')
            return redirect('geral:lista_servico')
    form = ServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)
