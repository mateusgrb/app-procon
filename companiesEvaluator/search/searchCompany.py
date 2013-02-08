# -*- coding:utf-8 -
# This Python file uses the encoding utf-8

from companiesEvaluator.models import *
from django.db.models import Q

def searchCompanies(companyName):
    '''
    Search a company (Fornecedor) with the closest name.
    
    input: companyName (String with the name or part of the name os a Company (Fornecedor))
    
    returns: List of Companies (Fornecedor).
    '''
    fornecedores = Fornecedor.objects.filter(Q(str_razao_social__icontains=companyName) | Q(str_nome_fantasia__icontains=companyName))
    
    return fornecedores


def searchCompanyInformations(companyName):
    ''' 
    Search a company (Fornecedor) which has str_nome_fantasia equals to companyName.
    
    input: companyName (String with the name or part of the name os a Company (Fornecedor))
    
    returns: the Company (Fornecedor).
    '''
    f = Fornecedor.objects.all()[0]
    return {fornecedor : f, evaluation_by_costumer_gender: 'evaluation_by_costumer_gender', evaluation_by_costumer_gender_year : 'evaluation_by_costumer_gender_year', evaluation_by_costumer_age_group : 'evaluation_by_costumer_age_group', evaluation_by_costumer_age_group_year : 'FALTA FAZER'}
    



