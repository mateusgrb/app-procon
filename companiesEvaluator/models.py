# -*- coding:utf-8 -
from django.db import models

class Fornecedor(models.Model):
    str_razao_social = models.CharField(max_length=180)
    str_nome_fantasia = models.CharField(max_length=180)
    tipo = models.IntegerField()
    numero_cnpj = models.CharField(max_length=20, unique=True)
    radical_cnpj = models.CharField(max_length=12)
    razao_social_rfb = models.CharField(max_length=180)
    nome_fantasia_rfb = models.CharField(max_length=180)
    cnae_principal = models.CharField(max_length=20)
    desc_cnae_principal = models.CharField(max_length=180)
    quantidade_reclamacoes = 0    
    percentual_reclamacoes_atendidas = 0
    percentual_reclamacoes_nao_atendidas = 0
    id_empresa = models.IntegerField()
 
    def __unicode__(self):
        return 'Razao social: ' + str(self.str_razao_social) + '. Nome Fantasia: ' + str(self.str_nome_fantasia) + '. CNPJ: ' + str(self.numero_cnpj) + '. Radical: ' + str(self.radical_cnpj)

class Regiao(models.Model):
    nome_regiao = models.CharField(max_length=20)
    
    def __unicode__(self):
        return str(self.nome_regiao)

class Reclamacao(models.Model):
    ano_calendario = models.IntegerField()
    data_arquivamento = models.DateTimeField()
    data_abertura = models.DateTimeField()
    uf = models.CharField(max_length=2)
    atendida = models.CharField(max_length=1)
    codigo_assunto = models.IntegerField()
    descricao_assunto = models.CharField(max_length=180)
    codigo_problema = models.IntegerField()
    descricao_problema = models.CharField(max_length=180)
    sexo_consumidor = models.CharField(max_length=1)
    faixa_etaria_consumidor = models.CharField(max_length=25)
    cep_consumidor = models.CharField(max_length=20)
    regiao = models.ForeignKey(Regiao)
    fornecedor = models.ForeignKey(Fornecedor)
    
    def __unicode__(self):
        return 'Ano: ' + str(self.ano_calendario) + '. Atendida: ' + str(self.atendida) + '. Regiao: <' + str(self.regiao) + '>. Fornecedor: <' + str(self.fornecedor) + '>.'
