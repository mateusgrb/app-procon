from companiesEvaluator.models import *
from companiesEvaluator.util.string_comparison import get_similarity
from copy import copy


def group_companies():
    fornecedores = Fornecedor.objects.all()
    set_id_empresas(fornecedores)

def set_id_empresas(fornecedores):
    novo_id = 1
    lista_com_id = []
    for fornecedor in fornecedores:
        if len(lista_com_id) > 0:
            # Passo 1, procurar se existe alguem com a razao social com similaridade maior que 70% na lista_com_id
            similars = []
            
            #Tratando caso das razoes sociais especiais.
            if (fornecedor.str_razao_social.startswith('BANCO DO BRASIL')):
                similars = filter(lambda elem: ((get_similarity(elem.str_razao_social, fornecedor.str_razao_social) > 0.8) and (elem.radical_cnpj == fornecedor.radical_cnpj)), lista_com_id)

            elif (fornecedor.str_razao_social.startswith('BANCO ')):
                similars = filter(lambda elem: get_similarity(elem.str_razao_social, fornecedor.str_razao_social) > 0.83, lista_com_id)

            elif (fornecedor.str_razao_social.startswith('MULTI')):
                similars = filter(lambda elem: get_similarity(elem.str_razao_social, fornecedor.str_razao_social) > 0.75, lista_com_id)

            else:
                similars = filter(lambda elem: get_similarity(elem.str_razao_social, fornecedor.str_razao_social) > 0.71, lista_com_id)


            if len(similars) == 0:
                fornecedor.id_empresa = novo_id
                novo_id = novo_id + 1
            else:
                if(get_similarity(fornecedor.str_razao_social, similars[0].str_razao_social) > 0.7):
                    fornecedor.id_empresa = similars[0].id_empresa
    
        else:
            fornecedor.id_empresa = novo_id
            novo_id = novo_id + 1
        
        lista_com_id.append(fornecedor)
        
    return lista_com_id    
    
    
    
def copy_list(old_list):
    new_list = []
    for elem in old_list:
        new_list.append(copy(elem))

    return new_list
