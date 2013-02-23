# -*- coding: utf-8 -*-
import difflib
import unicodedata

SUFFIXES = [u' ELETRONICA DA AMAZONIA LTDA', 
    u' ELETRONICS DA AMAZÔNIA LTDA', u' ELETRÔNICA DA AMAZÔNIA LTDA', 
    ' ELETRONICS DA AMAZONIA LTDA',u' ELETRÔNICA DA AMAZÔNIA S/A', 
    u' TELECOMUNICAÇÕES LTDA - ME',u' TELECOMUNICAÇOES LTDA - ME', 
    ' TELECOMUNICACOES LTDA', u' TELECOMUNICAÇÕES LTDA',
    ' TELECOMUNICACOES SA', u' TELECOMUNICAÇÕES SA',
    ' TELECOMUNICACOES S.A.', u' TELECOMUNICAÇÕES S.A.',
    ' TELECOMUNICACOES S/A', u' TELECOMUNICAÇÕES S/A',
    ' TELECOMUNICACOES S A', u' TELECOMUNICAÇÕES S A',
    ' LIVROS E INFORMATICA LTDA', u' LIVROS E INFORMÁTICA LTDA',
    ' LINHAS AEREAS S.A.', ' LINHAS AEREAS S/A', 
    ' LINHAS AEREAS S.A', ' LINHAS AEREAS SA', ' LINHAS AEREAS S A', 
    u' LINHAS AÉREAS S.A.', u' LINHAS AÉREAS SA', u' LINHAS AÉREAS S/A',
    u' LINHAS AÉREAS LTDA', u' LINHAS AEREAS',  
    u' LINHAS AÉREAS S.A', u' LINHAS AÉREAS S A', u' INFORMÁTICA LTDA', 
    u' INFORMÁTICA LTDA.', u' INFORMATICA LTDA', u' INFORMATICA LTDA.',
    u' INFORMÁTICA S/A', u' INFORMÁTICA S.A.', u' INFORMÁTICA SA', u' INFORMÁTICA S A',
    u' INFORMATICA S/A', u' INFORMATICA S.A.', u' INFORMATICA SA', u' INFORMATICA S A', 
    ' COMERCIO E INDUSTRIA', u' COMÉRCIO E INDUSTRIA',
    ' COMERCIAL S/A', ' COMERCIAL S.A.', ' COMERCIAL SA', 'COMERCIAL S A',
    ' COMERCIAL LTDA', ' COMERCIAL LTDA ME',
    u' PARTICIPAÇÕES LTDA', u' PARTICIPACOES LTDA',
    u' PARTICIPAÇÕES SA', u' PARTICIPACOES SA',
    u' PARTICIPAÇÕES S/A', u' PARTICIPACOES S/A',
    u' PARTICIPAÇÕES S.A.', u' PARTICIPACOES S.A.',
    u' ELETRÔNICOS LTDA', ' ELETRONICOS LTDA',
    ' COMPUTADORES LTDA', 'COMPUTADORES LTDA',
    ' EDICOES CULTURAIS LTDA', u' EDIÇÕES CULTURAIS LTDA',
    u' ASSISTÊNCIA TÉCNICA LTDA', u' ASSISTÊNCIA TECNICA LTDA', u' ASSISTENCIA TÉCNICA LTDA',
    u' ASSISTENCIA MEDICA LTDA', u' ASSISTENCIA MÉDICA LTDA',
    u' ASSISTENCIA TECNICA LTDA', u' COMERCIO E REPRESENTACOES LTDA',
    u' COMÉRCIO E REPRESENTAÇÕES LTDA', u' COMERCIO E REPRESENTAÇÕES LTDA',
    u' MOVEIS E ELETRODOMESTICOS LTDA', u' MÓVEIS E ELETRODOMÉSTICOS LTDA',
    u' COMERCIO DE MOVEIS LTDA', u' COMÉRCIO DE MÓVEIS LTDA',
    u' COMÉRCIO E INDUSTRIA LTDA', ' COMERCIO E INDUSTRIA LTDA.',
    ' CREDITO FINANCIAMENTO E INVESTIMENTO', u' CRÉDITO FINANCIAMENTO E INVESTIMENTO',
    u' ADMINISTRADORA DE CONSORCIO LTDA', u' ADMINISTRADORA DE CONSÓRCIO LTDA',
    u' ADMINISTRADORA DE CARTOES LTDA', u' ADMINISTRADORA DE CARTÕES LTDA',
    u' ADMINISTRADORA DE CARTOES S/A', u' ADMINISTRADORA DE CARTÕES S/A',
    u' ADMINISTRADORA DE CARTOES S.A', u' ADMINISTRADORA DE CARTÕES S.A',
    u' ADMINISTRADORA DE CARTOES S A', u' ADMINISTRADORA DE CARTÕES S A',
    u' VEICULOS PECAS E SERVICOS LTDA', u' VEÍCULOS PEÇAS E SERVIÇOS LTDA',
    u' ADMINISTRADORA DE CARTOES DE CREDITO LTDA', u' ADMINISTRADORA DE CARTÕES DE CREDITO LTDA',
    u' ADMINISTRADORA DE CARTOES DE CREDITO S/A', u' ADMINISTRADORA DE CARTÕES DE CREDITO S/A',
    u' ADMINISTRADORA DE CARTOES DE CREDITO S.A', u' ADMINISTRADORA DE CARTÕES DE CREDITO S.A',
    u' ADMINISTRADORA DE CARTOES DE CREDITO S A', u' ADMINISTRADORA DE CARTÕES DE CREDITO S A',
    u' ADMINISTRADORA DE CARTOES DE CRÉDITO LTDA', u' ADMINISTRADORA DE CARTÕES DE CRÉDITO LTDA',
    u' ADMINISTRADORA DE CARTOES DE CRÉDITO S/A', u' ADMINISTRADORA DE CARTÕES DE CRÉDITO S/A',
    u' ADMINISTRADORA DE CARTOES DE CRÉDITO S.A', u' ADMINISTRADORA DE CARTÕES DE CRÉDITO S.A',
    u' ADMINISTRADORA DE CARTOES DE CRÉDITO S A', u' ADMINISTRADORA DE CARTÕES DE CRÉDITO S A',
    u' ADMINISTRADORA DE CONSORCIO LTDA', u' ADMINISTRADORA DE CONSORCIOS LTDA',
    u' ADMINISTRADORA DE CONSÓRCIO LTDA', u' ADMINISTRADORA DE CONSÓRCIOS LTDA'
    u' COMERCIO E EXPORTACAO LTDA', u' COMÉRCIO E EXPORTAÇÃO LTDA',
    u' EDICOES CULTURAIS LTDA', u' EDICOES CULTURAIS LTDA ME',
    u' EDIÇÕES CULTURAIS LTDA', 
    u' COMERCIO DE ELETRO-ELETRONICOS', u' COMÉRCIO DE ELETRO-ELETRÔNICOS',
    u' COMERCIO IMPORTACAO E EXPORTACAO LTDA', u' COMERCIO IMPORTAÇÃO E EXPORTAÇÃO LTDA',
    u' IMPORTAÇÃO E EXPORTAÇÃO LTDA', u' IMPORTACAO E EXPORTACAO LTDA',
    u' COMERCIO DE VEICULOS LTDA', u' COMÉRCIO DE VEICULOS LTDA',
    u' COMERCIO DE VEICULOS LTDA ME', u' COMÉRCIO DE VEICULOS LTDA ME',
    u' EDUCACIONAL LTDA', u' IMP. E EXP. LTDA',
    ' UTILIDADES DOMESTICAS LTDA', ' UTILIDADES DOMESTICAS LTDA ME',
    u' UTILIDADES DOMÉSTICAS LTDA', u' UTILIDADES DOMÉSTICAS LTDA ME',
    u' ELETRODOMÉSTICOS LTDA', u' ELETRODOMESTICOS LTDA',
    u' IMOBILIARIOS LTDA', u' IMOBILIÁRIOS LTDA', u' IMOBILIÁRIOS S.A',
    u' IMOBILIARIOS S.A', u' IMOBILIARIOS S/A', u' IMOBILIÁRIOS S/A',
    u' CELULAR S.A.', 'CELULAR S/A', 'CELULAR LTDA', 'CELULAR LTDA - ME', 
    'CELULAR LTDA - EPP', 'CELULAR ME', 'CELULAR EPP',
    ' TELEFONES LTDA', ' TELEFONES LTDA ME',
    ' VEICULOS LTDA', u' VEÍCULOS LTDA',
    u' COMERCIO E REPRESENTACAO LTDA', u' COMÉRCIO E REPRESENTAÇÃO',
    ' ELETRONICS', u' ELETRÔNICA', u' ELETRONICA',
    ' LTDA ME', ' LTDA - ME', ' LTDA-M,E', ' LTDA-EPP', ' LTDA - EPP',  
    ' LTDA EPP', ' EPP', ' - EPP', ' -EPP', 
    ' LTDA', ' LTDA.', ' SA', ' S.A.', ' S/A', ' S/A.', ' LIMITADA', ' ME', ' S A']


PREFIXES = ['LOJAS ']

def remove_prefixes(word):
    '''
    Recieves one word on string format and returns the word without its prefix.
    The list of PREFIX is: ['BANCO ', 'LOJAS ']
    
    :param word
    :type word: str
    :return word without suffix
    :type word: str
    '''    
    
    for prefix in PREFIXES:
        if word.startswith(prefix):
            word = word.partition(prefix)[-1]
            break
    
    return word

def remove_suffixes(word):
    '''
    Recieves one word on string format and returns the word without its suffix.
    The list of SUFFIXES is:[x.str_razao_social for x in dic[1]]
    ['LTDA ME', 'LTDA - ME', 'LTDA-M,E', 'LTDA-EPP', 'LTDA - EPP',  
    'LTDA EPP', 'EPP', '- EPP', '-EPP', 'LTDA', 'LTDA.', 'SA', 
    'S.A.',  'S/A', 'S/A.', 'LIMITADA', 'ME', 'S A']
    
    :param word
    :type word: str
    :return word without suffix
    :type word: str
    '''    
    
    for suffix in SUFFIXES:
        if word.endswith(suffix):
            word = word.partition(suffix)[0]
            break
    
    return word

def remove_special_suffixes(word):
    '''
    Recieves one word on string format and returns the word without its suffix.
    
    :param word
    :type word: str
    :return word without suffix
    :type word: str
    '''    
    
    for suffix in ['DO BRASIL LTDA', 'BRASIL LTDA']:
        if word.endswith(suffix):
            word = word.partition(suffix)[0]
            break
    
    return word


def get_similarity(word1, word2):
    '''
    Receives two words on string format and returns the similarity between them.
    
    :param word1
    :type word1: str
    :param word2
    :type word2: str
    :return similarity
    :type similarity: float
    '''
    #print 'Similaridade entre ' + word1 + ' e ' + word2
    
    if(word1.endswith('DO BRASIL LTDA') or word1.endswith('DO BRASIL LIMITADA') or word1.endswith('BRASIL LTDA')) and (not word1.startswith('BANCO')):
        word1 = remove_special_suffixes(word1)
    
    if(word2.endswith('DO BRASIL LTDA') or word2.endswith('BRASIL LTDA')) and (not word2.startswith('BANCO')):
        word2 = remove_special_suffixes(word2)
    
    
    word1 = remove_suffixes(word1)
    word2 = remove_suffixes(word2)

    #Caso especial do Banco do Brasil.
    
    if ('BANCO DO BRASIL' in word1) and ('BANCO DO BRASIL' in word2):
        similarity = difflib.SequenceMatcher(None, word1.strip(), word2.strip()).ratio() + 0.3
    elif ('BANCO DO BRASIL' in word1) and not ('BANCO DO BRASIL' in word2):
        similarity = difflib.SequenceMatcher(None, word1.strip(), word2.strip()).ratio() - 0.5
    elif (not 'BANCO DO BRASIL' in word1) and ('BANCO DO BRASIL' in word2): 
        similarity = difflib.SequenceMatcher(None, word1.strip(), word2.strip()).ratio() - 0.5
    else:
        similarity = difflib.SequenceMatcher(None, word1.strip(), word2.strip()).ratio()
    
 
    return similarity
    
def get_similarity_first_words(word1, word2):
    '''
    Compares the similarity between the first 2 words from word1 and word2.
    
    :param word1
    :type word1: str
    :param word2
    :type word2: str
    :return similarity
    :type similarity: float
    '''
    similarity = 0
    word1 = remove_suffixes(word1)
    word2 = remove_suffixes(word2)
    #deixando a string com somente as duas primeiras palavras
    if(len(word1) > 2):
        word1 = word1.partition(' ')
        word1 = word1[0] + ' ' + word1[1]
        
    if(len(word2) > 2):
        word2 = word2.partition(' ')
        word2 = word2[0] + ' ' + word2[1]
        
    similarity = difflib.SequenceMatcher(None, word1, word2).ratio()
    
    return similarity

    
def remove_accents_lower(data):
    '''
    Removes the accents of each word and apply the function lower() to let them on lowercase mode.
    
    :param data
    :type data: str
    '''
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if ((unicodedata.category(x)[0] == 'L') | (unicodedata.category(x) == 'Pd'))).lower()
    
    
    
