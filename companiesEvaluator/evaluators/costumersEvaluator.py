# -*- coding:utf-8 -
# This Python file uses th encoding utf-8

from companiesEvaluator.models import Reclamacao

#This file contains functions that evaluate a company according to the Costumers sex,  age group, etc.

def get_evaluation_by_costumer_type(company, include_other_companies):
    '''
    This function gives the evaluation of a company based on the costumer type.
    1. Filters the results based on the 'str_nome_fantasia' of the company.
    
    2. The return contains the amount of all claims of every year for the company.
    
    Input: 
        company - an ID that represents the company.
        include_other_companies - flag that determines whether the evaluation should include consumers of type company ("pessoa jurídica").
        
    returns: A dictionary with the name of the region and the quantity of complaints coming from there.
    Example: {'Mulheres'=100, 'Homens'=500, 'Outras empresas'=700}
    or
             {'Mulheres'=100, 'Homens'=500}
    '''
    return 0
    

