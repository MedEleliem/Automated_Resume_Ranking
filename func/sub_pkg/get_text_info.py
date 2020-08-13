import os
import re

from txt_preproc import get_low
from txt_preproc import main_PreProc

from doc_2_txt import convert_pdf_to_txt

from txt_catego import tokenizer
from txt_catego import bigrams_
from txt_catego import trigrams_ 


def path_selector(path):
    """ this function will return a list of all files paths with pdf format"""
    L=[]
    
    if type(path) == str and path.endswith('.pdf') == True:
        base = os.path.basename(path)
        return {'name': get_low(os.path.splitext(base)[0]), 'path': path}
    
    
    elif type(path) == str and path.endswith('.pdf') == False:
        for filename in os.listdir(path):
            if filename.endswith('.pdf'):
                base = os.path.basename(filename)
                L.append({'name': get_low(os.path.splitext(base)[0]), 'path': os.path.join(path, filename)})
    return L


def insert_text_into(path):
    List = []
    path_ = path_selector(path)
    if type(path_) == list :  
        
        for i in path_:
            text = convert_pdf_to_txt(i.get('path'))
            preproceced_text = main_PreProc(text)
            tokens = tokenizer(preproceced_text)
            bigrams = bigrams_(preproceced_text, tokens)
            trigrams = trigrams_(preproceced_text, tokens)
            #counter = Counter(tokens)
            #most_freq = counter.most_common(1) 
            List.append(
                         {
                          'name' : re.sub('[\d+ .pdf !"#$%&()*+,./:;<=>?@[\]^_`{|}~‘’•]','',i.get('name')),
                          'raw_text' : text,
                          'tokens' : tokens,
                          'bigrams': bigrams,
                          'trigrams': trigrams,
                          #'most_common_word' : most_freq[0][0],
                          #'word_freq' : most_freq[0][1]/len(tokens),
                          }
                        )
                         
        return List
    elif type(path_) == dict : 
        text = convert_pdf_to_txt(path_.get('path'))
        preproceced_text = main_PreProc(text)
        tokens = tokenizer(preproceced_text)
        bigrams = bigrams_(preproceced_text, tokens)
        trigrams = trigrams_(preproceced_text, tokens)
        #counter = Counter(tokens)
        #most_freq = counter.most_common(1) 
        element = {
                          'name' : re.sub('[\d+ .pdf !"#$%&()*+,./:;<=>?@[\]^_`{|}~‘’• CV cv ]','',path_.get('name')),
                          'raw_text' : text,
                          'tokens' : tokens,
                          'bigrams': bigrams,
                          'trigrams': trigrams,
                          #'most_common_word' : most_freq[0][0],
                          #'word_freq' : most_freq[0][1]/len(tokens),
                  } 
        
        List.append(element)
        return element