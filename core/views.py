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

    estrategia = Estrategia(cotacao_minima=100)

    Result.result()

    form = SearchForm()
    result = Result.tabela_result
    filtro = SaveForm()
    response = []

    context = {'list':result, 'search':form, 'filter':filtro}

    # Obtém a URL da view nova
    url_nova = reverse('index') 

    # Redireciona para a view nova com o novo contexto
    return redirect(url_nova, context=context)
