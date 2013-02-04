# -*- coding:utf-8 -
from django.db import models

class Fornecedor(models.Model):
    str_razao_social = models.CharField(max_length=180, primary_key=True)
    str_nome_fantasia = models.CharField(max_length=180)
    tipo = models.IntegerField()
    numero_cnpj = models.CharField(max_length=20)
    radical_cnpj = models.CharField(max_length=12)
    razao_social_rfb = models.CharField(max_length=180)
    nome_fantasia_rfb = models.CharField(max_length=180)
    cnae_principal = models.CharField(max_length=20)
    desc_cnae_principal = models.CharField(max_length=180)

class Reclamacao(models.Model):
    ano_calendario = models.IntegerField()
    data_arquivamento = models.DateTimeField()
    data_abertura = models.DateTimeField()
    codigo_regiao = models.CharField(max_length=20)
    regiao = models.CharField(max_length=20)
    uf = models.CharField(max_length=2)
    atendida = models.CharField(max_length=1)
    codigo_assunto = models.IntegerField()
    descricao_assunto = models.CharField(max_length=180)
    codigo_problema = models.IntegerField()
    descricao_problema = models.CharField(max_length=180)
    sexo_consumidor = models.CharField(max_length=1)
    faixa_etaria_consumidor = models.CharField(max_length=25)
    cep_consumidor = models.CharField(max_length=20)
    fornecedor = models.ForeignKey(Fornecedor)
