# -*- coding:utf-8 -
from companiesEvaluator.models import Reclamacao, Fornecedor
from django.db import connection

def rank_by_complains(limit=20):
    query = 'SELECT f.id, f.str_razao_social, f.radical_cnpj, (select count(r.id) FROM companiesEvaluator_reclamacao r where r.fornecedor_id = f.id) as qtd_reclamacoes FROM companiesEvaluator_fornecedor f group by f.radical_cnpj order by qtd_reclamacoes desc limit ' + str(limit)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return list(result)
