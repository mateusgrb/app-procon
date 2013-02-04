# -*- coding:utf-8 -
import csv
import transaction
from companiesEvaluator.models import Fornecedor, Reclamacao

def import_data(filename):
    file_read = open(filename, "rb")
    reader = csv.reader(file_read, delimiter=';')
    transaction.begin()
    for row in list(reader)[1:]:
        f = Fornecedor(str_razao_social=row[6].decode('windows-1252'), str_nome_fantasia=row[7].decode('windows-1252'), tipo=row[8],
            numero_cnpj=row[9], radical_cnpj=row[10], razao_social_rfb=row[11].decode('windows-1252'), nome_fantasia_rfb=row[12].decode('windows-1252'), 
            cnae_principal=row[13], desc_cnae_principal=row[14].decode('windows-1252'))
        f.save()
        r = Reclamacao(ano_calendario=row[0], data_arquivamento=row[1], data_abertura=row[2],
            codigo_regiao=row[3], regiao=row[4], uf=row[5], atendida=row[15], codigo_assunto=row[16],
            descricao_assunto=row[17].decode('windows-1252'), codigo_problema=row[18], descricao_problema=row[19].decode('windows-1252'),
            sexo_consumidor=row[20], faixa_etaria_consumidor=row[21].decode('windows-1252'),
            cep_consumidor=row[22], fornecedor=f)
        r.save() 
    transaction.commit()   
    file_read.close() 
    print 'Done!'
