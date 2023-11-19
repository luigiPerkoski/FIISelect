from django.shortcuts import redirect, render, HttpResponse
from .controller import Result, Estrategia
from django.urls import reverse
from .forms import SaveForm, SearchForm

def index(request):

    Result.result()
    result = Result.tabela_result
    filtro = SaveForm()
    response = []

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            for c in result:
                if query.upper() in c['papel']:
                    response.append(c)
            result = response
        else:
            result = Result.tabela_result
    else:
        form = SearchForm()
        result = Result.tabela_result

    context = {'list':result, 'search':form, 'filter':filtro}
    
    return render(request, 'core/pages/index.html', context)

def filter_FII(request):

    estrategia = Estrategia()

    if request.method == 'POST':
        form = SaveForm(request.POST)
        if form.is_valid():
            cotacao_minima = form.cleaned_data['cotacao']
            ffo_yield_minima = form.cleaned_data['ffo_yield']
            dividend_yield_minima = form.cleaned_data['dividend_yield']
            p_vp_minima = form.cleaned_data['p_vp']
            valor_mercado_minimo = form.cleaned_data['valor_mercado']
            liquidez_minima = form.cleaned_data['liquidez']
            cap_rate_minimo = form.cleaned_data['cap_rate']
            vacancia_minima = form.cleaned_data['vacancia']

            estrategia = Estrategia(cotacao_minima=cotacao_minima, ffo_yield_minima=ffo_yield_minima, 
            dividend_yield_minimo= dividend_yield_minima,
            p_vp_minimo= p_vp_minima,
            valor_mercado_minimo= valor_mercado_minimo,
            liquidez_minima= liquidez_minima,
            cap_rate_minimo= cap_rate_minimo,
            vacancia_minima= vacancia_minima)

    Result.result(estrategia=estrategia)

    form = SearchForm()
    result = Result.tabela_result
    filtro = SaveForm()
    response = []

    context = {'list':result, 'search':form, 'filter':filtro}

    return render(request, 'core/pages/index.html', context)
