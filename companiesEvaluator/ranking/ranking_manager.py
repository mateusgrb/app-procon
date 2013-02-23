# -*- coding:utf-8 -
from companiesEvaluator.models import Reclamacao, Fornecedor
from django.db import connection

def rank_by_complaints(limit=20):
    query = """SELECT f.id, f.str_razao_social,f.str_nome_fantasia, f.radical_cnpj, (select count(r.id) 
            FROM companiesEvaluator_reclamacao r where r.fornecedor_id = f.id) as qtd_reclamacoes 
            FROM companiesEvaluator_fornecedor f group by f.radical_cnpj order by qtd_reclamacoes 
            desc limit """ + str(limit)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    result_list = [__create_row_ranking_by_complaints(row) for row in result]
    return result_list

def __create_row_ranking_by_complaints(row):
    if (row[2] is None) or (row[2] == 'NULL'):
        company_name = row[1]
    else:
        company_name = row[2] 
    f = Fornecedor(id=row[0], str_nome_fantasia=company_name)
    f.quantidade_reclamacoes = row[4]
    return f

def rank_by_adressed_complaints(limit=20):
    query = """SELECT f.id, f.str_razao_social,f.str_nome_fantasia, f.radical_cnpj, ((select count(r.id) 
            FROM companiesEvaluator_reclamacao r where r.fornecedor_id = f.id and r.atendida = 'S')/
            (select count(r.id) FROM companiesEvaluator_reclamacao r where r.fornecedor_id = f.id))*100 
            as percentual_reclamacoes_atendidas FROM companiesEvaluator_fornecedor f 
            group by f.radical_cnpj order by percentual_reclamacoes_atendidas desc limit """ + str(limit)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    result_list = [__create_row_ranking_by_adressed_complaints(row) for row in result]
    return result_list
    pass

def __create_row_ranking_by_adressed_complaints(row):
    if (row[2] is None) or (row[2] == 'NULL'):
        company_name = row[1]
    else:
        company_name = row[2] 
    f = Fornecedor(id=row[0], str_nome_fantasia=company_name)
    f.percentual_reclamacoes_atendidas = int(row[4])
    return f

def rank_by_non_adressed_complaints(limit=20):
    query = """SELECT f.id, f.str_razao_social,f.str_nome_fantasia, f.radical_cnpj, ((select count(r.id) 
            FROM companiesEvaluator_reclamacao r where r.fornecedor_id = f.id and r.atendida = 'N')/
            (select count(r.id) FROM companiesEvaluator_reclamacao r where r.fornecedor_id = f.id))*100 
            as percentual_reclamacoes_nao_atendidas FROM companiesEvaluator_fornecedor f 
            group by f.radical_cnpj order by percentual_reclamacoes_nao_atendidas desc limit """ + str(limit)
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    result_list = [__create_row_ranking_by_non_adressed_complaints(row) for row in result]
    return result_list

def __create_row_ranking_by_non_adressed_complaints(row):
    if (row[2] is None) or (row[2] == 'NULL'):
        company_name = row[1]
    else:
        company_name = row[2] 
    f = Fornecedor(id=row[0], str_nome_fantasia=company_name)
    f.percentual_reclamacoes_nao_atendidas = int(row[4])
    return f

def rank_by_common_problems(limit=20):
    query = """SELECT descricao_problema, COUNT(*) FROM companiesEvaluator_reclamacao 
            GROUP BY descricao_problema ORDER BY COUNT(*) DESC LIMIT """ + str(limit) 
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    result_list = list(result) 
    return result_list
