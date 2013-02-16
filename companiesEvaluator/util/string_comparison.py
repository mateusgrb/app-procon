# -*- coding: utf-8 -*-
import difflib
import unicodedata

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
	similarity = difflib.SequenceMatcher(None, word1, word2).ratio()
	
	return similarity
		
def remove_accents_lower(data):
	'''
	Removes the accents of each word and apply the function lower() to let them on lowercase mode.
	
	:param data
	:type data: str
	'''
	return ''.join(x for x in unicodedata.normalize('NFKD', data) if ((unicodedata.category(x)[0] == 'L') | (unicodedata.category(x) == 'Pd'))).lower()
