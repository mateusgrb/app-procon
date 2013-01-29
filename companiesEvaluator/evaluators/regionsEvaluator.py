# -*- coding:utf-8 -
# This Python file uses th encoding utf-8

from companiesEvaluator.models import Reclamacao

#This file contains functions that evaluate a company according to the Region complaints.
NORTE = 'Norte'
NORDESTE = 'Nordeste'
SUL = 'Sul'
C_OESTE = 'Centro-Oeste'
SUDESTE = 'Sudeste'

def get_evaluation_by_region(company):
    '''
    This function gives the evaluation of a company based on the evaluation region.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims of every year for the company.
    
    Input: company - an ID that represents the company.
    
    returns: A dictionary with the name of the region and the percentage of complaints coming from there.
    Example: {'Norte'=100, 'Nordeste'=500, 'Centro-Oeste'=700, 'Sul'=1000, 'Sudeste'=3000}
    '''
    
    #Esse filtro pode mudar.
   
    norte_evaluation = Reclamacao.objects.filter(str_nome_fantasia=company, regiao=NORTE)
    nordeste_evaluation = Reclamacao.objects.filter(str_nome_fantasia=company, regiao=NORDESTE)
    centro_oeste_evaluation = Reclamacao.objects.filter(str_nome_fantasia=company, regiao=C_OESTE)
    sul_evaluation = Reclamacao.objects.filter(str_nome_fantasia=company, regiao=SUL)
    sudeste_evaluation = Reclamacao.objects.filter(str_nome_fantasia=company, regiao=SUDESTE)
    
    return {NORTE: len(norte_evaluation), NORDESTE: len(nordeste_evaluation), C_OESTE: len(centro_oeste_evaluation), SUL: len(sul_evaluation), SUDESTE: len(sudeste_evaluation)}
    
#def get_evaluation_by_region_year(company, year)
#def get_evaluation_by_region_gender(company, gender)

    
