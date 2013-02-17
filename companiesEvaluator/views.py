# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from companiesEvaluator.models import Fornecedor, Reclamacao
from forms import SearchForm
from companiesEvaluator.ranking.ranking_manager import rank_by_complaints, rank_by_adressed_complaints, rank_by_non_adressed_complaints, rank_by_common_problems
from django.shortcuts import render
from companiesEvaluator.search.search_company import search_companies
	  	
def search(request):	  	
    if request.method == 'POST':
	 form = SearchForm(request.POST)
         if form.is_valid():
            keyword = form.cleaned_data['keyword']
            fornecedores = search_companies(keyword)
            return render(request, 'index.html', {
                'form': form,
                'fornecedores': fornecedores,
            })
    else:
        form = SearchForm(auto_id=False)
    
    return render(request, 'index.html', {
        'form': form,  	
    })
	  	
def ranking(request):
    companies_by_complaints = rank_by_complaints()
    companies_by_adressed_complaints = rank_by_adressed_complaints()
    companies_by_non_adressed_complaints = rank_by_non_adressed_complaints()
    common_problems = rank_by_common_problems()
    return render(request, 'ranking.html', {
        'fornecedores_reclamacoes': companies_by_complaints,
        'fornecedores_reclamacoes_atendidas': companies_by_adressed_complaints,
        'fornecedores_reclamacoes_nao_atendidas': companies_by_non_adressed_complaints,
        'problemas_comuns': common_problems,
    })
	  	
def compare(request):
    return render(request, 'compare.html')
	  	
def comofunciona(request):
    return render(request, 'comofunciona.html')
	  	
def procon(request):
    return render(request, 'procon.html')
	  	
def charts(request):
    return render(request, 'charts.html')
