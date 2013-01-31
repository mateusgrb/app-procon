# -*- coding:utf-8 -
# This Python file uses th encoding utf-8

from companiesEvaluator.models import Reclamacao

#This file contains functions that evaluate a company according to the Costumers sex,  age group, etc.

#constants
WOMEN_SEARCH='F' #representing the "Feminino" set.
MEN_SEARCH='M' #representing the "Masculino" set.
WOMEN='Mulheres'
MEN='Homens'


def get_evaluation_by_costumer_gender(company):
    '''
    This function gives the evaluation of a company based on the costumer gender.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims of every year for the company.
    
    Input: 
        company - an ID that represents the company.
        include_other_companies - flag that determines whether the evaluation should include consumers of type company ("pessoa jurídica").
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'Mulheres'=100, 'Homens'=500}
    '''
    mulheres_evaluation = Reclamacao.objects.filter(sexo_consumidor=WOMEN_SEARCH, fornecedor__str_nome_fantasia=company)
    homens_evaluation = Reclamacao.objects.filter(sexo_consumidor=MEN_SEARCH, fornecedor__str_nome_fantasia=company)
    #outras_empresas_evaluation = Reclamacao.objects.filter(sexo_consumidor='N') 
    
    return {WOMEN: len(mulheres_evaluation), MEN: len(homens_evaluation)}
    
def get_evaluation_by_costumer_gender_year(company):
    '''
    This function gives the evaluation of a company based on the costumer type.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims related to the year.
    
    Input: 
        company - an ID that represents the company.
        include_other_companies - flag that determines whether the evaluation should include consumers of type company ("pessoa jurídica").
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'Mulheres'=100, 'Homens'=500}
    '''
    mulheres_evaluation = Reclamacao.objects.filter(sexo_consumidor=WOMEN_SEARCH, fornecedor__str_nome_fantasia=company, ano_calendario=year)
    homens_evaluation = Reclamacao.objects.filter(sexo_consumidor=MEN_SEARCH, fornecedor__str_nome_fantasia=companyano_calendario=year)
    #outras_empresas_evaluation = Reclamacao.objects.filter(sexo_consumidor='N') 
    
    return {WOMEN: len(mulheres_evaluation), MEN: len(homens_evaluation)}
