from django.shortcuts import render, HttpResponse
from .controller import Result
from .forms import SaveForm

result = Result.tabela_result

def index(request):

    if request.method == 'POST':
        form = SaveForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SaveForm()

    context = {'list':result, 'form':form}
    
    return render(request, 'core/pages/index.html', context)