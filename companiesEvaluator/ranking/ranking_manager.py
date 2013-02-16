# -*- coding:utf-8 -
from companiesEvaluator.models import Reclamacao, Fornecedor
from django.db import connection

def rank_by_complaints(limit=20):
    query = 'SELECT f.id, f.str_razao_social, f.radical_cnpj, (select count(r.id) FROM companiesEvaluator_reclamacao r where r.fornecedor_id = f.id) as qtd_reclamacoes FROM companiesEvaluator_fornecedor f group by f.radical_cnpj order by qtd_reclamacoes desc limit ' + str(limit)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    result_list = [__create_ranking_row(row) for row in result]
    return result_list

def __create_ranking_row(row):
    f = Fornecedor(id=row[0], str_razao_social=row[1], radical_cnpj=row[2])
    f.quantidade_reclamacoes = row[3]
    return f
