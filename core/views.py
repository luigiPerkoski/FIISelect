from django.shortcuts import render, HttpResponse
from .controller import Result
from .forms import SaveForm, SearchForm

def index(request):

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