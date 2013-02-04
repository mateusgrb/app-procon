# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from companiesEvaluator.models import Fornecedor, Reclamacao

def index(request):
	return render(request, 'index.html')

def ranking(request):
	return render(request, 'ranking.html')

def compare(request):
	return render(request, 'compare.html')

def comofunciona(request):
	return render(request, 'comofunciona.html')

def procon(request):
	return render(request, 'procon.html')

def charts(request):
	return render(request, 'charts.html')
