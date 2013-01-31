# -*- coding:utf-8 -
import csv
from companiesEvaluator.models import Fornecedor, Reclamacao

def import_data(filename):
    file_read = open(filename, "rb")
    reader = csv.reader(file_read, delimiter=';')
    for row in list(reader)[1:]:
        f = Fornecedor(str_razao_social=row[6].decode('ISO-8859-1'), str_nome_fantasia=row[7].decode('ISO-8859-1'), tipo=row[8],
            numero_cnpj=row[9], radical_cnpj=row[10], razao_social_rfb=row[11].decode('ISO-8859-1'), nome_fantasia_rfb=row[12].decode('ISO-8859-1'), 
            cnae_principal=row[13], desc_cnae_principal=row[14].decode('ISO-8859-1'))
        f.save()
        r = Reclamacao(ano_calendario=row[0], data_arquivamento=row[1], data_abertura=row[2],
            codigo_regiao=row[3], regiao=row[4], uf=row[5], atendida=row[15], codigo_assunto=row[16],
            descricao_assunto=row[17].decode('ISO-8859-1'), codigo_problema=row[18], descricao_problema=row[19].decode('ISO-8859-1'),
            sexo_consumidor=row[20], faixa_etaria_consumidor=row[21],
            cep_consumidor=row[22], fornecedor=f)
        r.save()     
