from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

import re
import spacy



def tokenizer(text,lang):
    if lang == 'fr':
        nlp = spacy.load("fr_core_news_sm")
    elif lang == 'en':
        nlp = spacy.load("en_core_web_sm")
        
    doc = nlp(text)
    L=[]
    for token in doc : 
        if re.search(' +', token.text)==None:
            L.append(token.text)
    return L


def bigrams_(text, tokens):
    l=[]

    finder = BigramCollocationFinder.from_words(tokens)
    
    a = finder.nbest(BigramAssocMeasures.likelihood_ratio,1000)    
    for i in range(len(a)):
        l.append(a[i][0]+' '+a[i][1])
    return l
    


def trigrams_(text, tokens):
    l=[]
     
    finder = TrigramCollocationFinder.from_words(tokens)

    a = finder.nbest(TrigramAssocMeasures.likelihood_ratio,1000)    
    for i in range(len(a)):
        l.append(a[i][0]+' '+a[i][1]+' '+a[i][2])
    
    return l
    