# -*- coding:utf-8 -
# This Python file uses the encoding utf-8

from companiesEvaluator.models import Reclamacao

#This file contains functions that evaluate a company according to the Region complaints.

#constants
NORTE = 'Norte'
NORDESTE = 'Nordeste'
SUL = 'Sul'
C_OESTE = 'Centro-oeste'
SUDESTE = 'Sudeste'

def get_evaluation_by_region(company):
    '''
    This function gives the evaluation of a company (Fornecedor) based on the evaluation region.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims of every year for the company.
    
    Input: company - an ID that represents the company.
    
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'Norte':100, 'Nordeste':500, 'Centro-Oeste':700, 'Sul':1000, 'Sudeste':3000}
    '''
    
    #Esse filtro pode mudar

    norte_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=NORTE)
    nordeste_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=NORDESTE)
    centro_oeste_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=C_OESTE)
    sul_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=SUL)
    sudeste_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=SUDESTE)
    
    return {NORTE: len(norte_evaluation), NORDESTE: len(nordeste_evaluation), C_OESTE: len(centro_oeste_evaluation), SUL: len(sul_evaluation), SUDESTE: len(sudeste_evaluation)}

    
def get_evaluation_by_region_year(company, year):
    '''
    This function gives the evaluation of a company (Fornecedor) based on the evaluation region and the specified year.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims related to the year.
    
    Input: 
        company - an ID that represents the company.
        year - an Integer that represents the year of the complaints.
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'Norte':100, 'Nordeste':500, 'Centro-Oeste':700, 'Sul':1000, 'Sudeste':3000}
    '''
    
    #For now, the query search based on Fornecedors' str_nome_fantasia.

    norte_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=NORTE, ano_calendario=year)
    nordeste_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=NORDESTE, ano_calendario=year)
    centro_oeste_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=C_OESTE, ano_calendario=year)
    sul_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=SUL, ano_calendario=year)
    sudeste_evaluation = Reclamacao.objects.filter(fornecedor__str_nome_fantasia=company, regiao=SUDESTE, ano_calendario=year)
 
    return {NORTE: len(norte_evaluation), NORDESTE: len(nordeste_evaluation), C_OESTE: len(centro_oeste_evaluation), SUL: len(sul_evaluation), SUDESTE: len(sudeste_evaluation)}
    
