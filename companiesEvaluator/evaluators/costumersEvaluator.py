# -*- coding:utf-8 -
# This Python file uses the encoding utf-8

from companiesEvaluator.models import Reclamacao

#This file contains functions that evaluate a company according to the Costumers sex,  age group, etc.

#constants
WOMEN_SEARCH='F' #representing the "Feminino" set.
MEN_SEARCH='M' #representing the "Masculino" set.
WOMEN='Mulheres'
MEN='Homens'
group_20='até 20 anos' #É importante verificar se no banco está salvando com acentos!!!
group_21_30='entre 21 a 30 anos'
group_31_40='entre 31 a 40 anos'
group_41_50='entre 41 a 50 anos'
group_51_60='entre 51 a 60 anos'
group_61_70='entre 61 a 70 anos'
group_70='mais de 70 anos'
group_nf='Nao informada'


def get_evaluation_by_costumer_gender(company):
    '''
    This function gives the evaluation of a company based on the costumer gender.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims of every year for the company.
    
    Input: 
        company - an ID that represents the company.
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'Mulheres':100, 'Homens':500}
    '''
    mulheres_evaluation = Reclamacao.objects.filter(sexo_consumidor=WOMEN_SEARCH, fornecedor__str_nome_fantasia=company)
    homens_evaluation = Reclamacao.objects.filter(sexo_consumidor=MEN_SEARCH, fornecedor__str_nome_fantasia=company)
    
    return {WOMEN: len(mulheres_evaluation), MEN: len(homens_evaluation)}
    
def get_evaluation_by_costumer_gender_year(company, year):
    '''
    This function gives the evaluation of a company based on the costumer type.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims related to the year.
    
    Input: 
        company - an ID that represents the company.
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'Mulheres':100, 'Homens':500}
    '''
    mulheres_evaluation = Reclamacao.objects.filter(sexo_consumidor=WOMEN_SEARCH, fornecedor__str_nome_fantasia=company, ano_calendario=year)
    homens_evaluation = Reclamacao.objects.filter(sexo_consumidor=MEN_SEARCH, fornecedor__str_nome_fantasia=company, ano_calendario=year) 
    
    return {WOMEN: len(mulheres_evaluation), MEN: len(homens_evaluation)}
    
    
def get_evaluation_by_costumer_age_group(company):
    '''
    This function gives the evaluation of a company based on the costumer age group.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims related to the year..
    
    Input: 
        company - an ID that represents the company.
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'0-20':100, '21-30': 200, '31-40':800, '41-50':1560, '51-60':20, '61-70':200, '70+':80, 'Desconhecido':30}
    '''
    
    group_20_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_20)  
    group_21_30_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_21_30)
    group_31_40_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_31_40)
    group_41_50_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_41_50)
    group_51_60_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_51_60)
    group_61_70_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_61_70)
    group_70_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_70)
    group_nf_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_nf)
    
    return {group_20: len(group_20_evaluation), group_21_30: len(group_21_30_evaluation), group_31_40: len(group_31_40_evaluation), group_41_50: len(group_41_50_evaluation), group_51_60: len(group_51_60_evaluation), group_61_70: len(group_61_70_evaluation), group_70: len(group_70_evaluation), group_nf: len(group_nf_evaluation)}
    
def get_evaluation_by_costumer_age_group_year(company, year):
    '''
    This function gives the evaluation of a company based on the costumer age group.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims of every year for the company.
    
    Input: 
        company - an ID that represents the company.
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'0-20':100, '21-30': 200, '31-40':800, '41-50':1560, '51-60':20, '61-70':200, '70+':80, 'Desconhecido':30}
    '''
    
    group_20_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_20, ano_calendario=year)  
    group_21_30_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_21_30, ano_calendario=year)
    group_31_40_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_31_40, ano_calendario=year)
    group_41_50_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_41_50, ano_calendario=year)
    group_51_60_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_51_60, ano_calendario=year)
    group_61_70_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_61_70, ano_calendario=year)
    group_70_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_70, ano_calendario=year)
    group_nf_evaluation = Reclamacao.objects.filter(faixa_etaria_consumidor=group_nf, ano_calendario=year)
    
    return {group_20: len(group_20_evaluation), group_21_30: len(group_21_30_evaluation), group_31_40: len(group_31_40_evaluation), group_41_50: len(group_41_50_evaluation), group_51_60: len(group_51_60_evaluation), group_61_70: len(group_61_70_evaluation), group_70: len(group_70_evaluation), group_nf: len(group_nf_evaluation)}

