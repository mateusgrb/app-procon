# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from companiesEvaluator.models import Fornecedor, Reclamacao
from forms import SearchForm
from companiesEvaluator.ranking.ranking_manager import rank_by_complaints
	  	
def search(request):	  	
    if request.method == 'POST':
	 form = SearchForm(request.POST)
         if form.is_valid():
             keyword = form.cleaned_data['keyword']
             f = Fornecedor.objects.filter(Q(str_razao_social__icontains=keyword)
                 | Q(str_nome_fantasia__icontains=keyword))
	     return render(request, 'index.html', {
                'form': form,
                'fornecedores': f,
            })  	
    else:
        form = SearchForm(auto_id=False)
    
    return render(request, 'index.html', {
        'form': form,  	
    })
	  	
def ranking(request):
    result = rank_by_complaints()
    return render(request, 'ranking.html', {
        'fornecedores': result,
    })
	  	
def compare(request):
    return render(request, 'compare.html')
	  	
def comofunciona(request):
    return render(request, 'comofunciona.html')
	  	
def procon(request):
    return render(request, 'procon.html')
	  	
def charts(request):
    return render(request, 'charts.html')
