from django.shortcuts import render, HttpResponse
from .controller import result

result = result()

def index(request):

    context = {'list':result}
    
    return render(request, 'core/pages/index.html', context)