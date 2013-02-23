# -*- coding:utf-8 -
# This Python file uses the encoding utf-8

from companiesEvaluator.models import *
from django.db.models import Q
import copy

def search_companies(companyName):
    '''
    Search a company (Fornecedor) with the similar names .
    
    input: companyName (String with the name or part of the name os a Company (Fornecedor))
    
    returns: List of Companies (Fornecedor).
    '''
    fornecedores = list(Fornecedor.objects.filter(Q(str_razao_social__icontains=companyName) | Q(str_nome_fantasia__icontains=companyName)))
    fornecedores = filter_list(fornecedores)
    
    return fornecedores


def filter_list(fornecedores):
    filtered_list = []
    for fornecedor in fornecedores:
        if(fornecedor.str_nome_fantasia.lower() == 'null'):
                fornecedor.str_nome_fantasia = copy.copy(fornecedor.str_razao_social)
        if (not (contains_company(filtered_list, fornecedor))):
            filtered_list.append(fornecedor)
            
    return filtered_list
    
def contains_company(filtered_list, fornecedor):
    retorno = False
    #dict(zip(lista, lista)).keys()
    if(len(filtered_list) > 0):
        lista_razao_social = map(lambda elem: elem.str_razao_social, filtered_list)
        lista_nome_fantasia = map(lambda elem: elem.str_nome_fantasia, filtered_list)

        if (fornecedor in filtered_list):
            #Caso 1: verifica se não existe nenhum fornecedor igual ao que se está tentando adicionar
            retorno = True
        elif (fornecedor.str_nome_fantasia in lista_nome_fantasia):
            #Caso 2: verificar se o nome fantasia do fornecedor está incluido na lista
            retorno = True
        elif (fornecedor.str_razao_social in lista_razao_social): 
            #Caso 3: Verificar se a razao social do fornecedor está incluido na lista
            retorno = True
    else:
        retorno = False    
    
    return retorno    

def search_company_informations(companyName):
    ''' 
    Search a company (Fornecedor) which has str_nome_fantasia equals to companyName.
    
    input: companyName (String with the name or part of the name os a Company (Fornecedor))
    
    returns: the Company (Fornecedor).
    '''
    f = Fornecedor.objects.all()[0]
    return {fornecedor : f, evaluation_by_costumer_gender: 'evaluation_by_costumer_gender', evaluation_by_costumer_gender_year : 'evaluation_by_costumer_gender_year', evaluation_by_costumer_age_group : 'evaluation_by_costumer_age_group', evaluation_by_costumer_age_group_year : 'FALTA FAZER'}
    



