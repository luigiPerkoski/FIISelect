from django.shortcuts import render, HttpResponse
from .controller import Result

Result.result()

result = Result.tabela_result

def index(request):

    context = {'list':result}
    
    return render(request, 'core/pages/index.html', context)