#!/usr/bin/env python
# coding: utf-8

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import re
import spacy
nlp = spacy.load("en_core_web_sm")




def convert_pdf_to_txt(path):""" THIS FUNCTION ALLOW US TO CONVERT DIFFERENTS TYPES OF PDF FILE INTO TEXT """
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 2
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()
    text = re.sub('\n', ' ', text)
    

    fp.close()
    device.close()
    retstr.close()
    return text


def remove_SpeChar(text): """ ANY SPECIAL WORDS WILL BE REMOVED """
    text = re.sub('\[.*?\]', '', text)
    text = re.sub(r'[^\w]', ' ', text)
    text= re.sub('\S*@\S*\s?', '', text)
    text = re.sub('[!"#$%&()*+,./:;<=>?@[\]^_`{|}~‘’•]', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = " ".join(text.split())
    return text


def remove_StopWords(text): """ ENGLISH STOPWRODS WILL BE REMOVED """
    sentence = nlp(text)
    filtered_sentence = ''
    token_list = []
    for token in sentence : 
        token_list.append(token.text)
    for word in token_list:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop == False :
            filtered_sentence += ' '+word
    return filtered_sentence


def get_lem(text): """ WORDS WILL BE LEMMATIZED TO FACILITE MATCHING WORDS """
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

def remove_Ent(text): """ PERSONAL NAMES, SPECEFIC DATES, COUNTRIES CITIES AND ADRESSES WILL BE REMOVED """
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == 'DATE' : 
            text = re.sub(ent.text,' ',text)
        elif ent.label_ == 'PERSON' : 
            text = re.sub(ent.text,' ',text)
        elif ent.label_ == 'GPE' : 
            text = re.sub(ent.text,' ',text)
    return text

def get_low(text):
    return text.lower()
            

def main_(path): """ FINALLY OUR RESUME IS READY """
    text = convert_pdf_to_txt(path)
    text = remove_SpeChar(text)
    text = remove_StopWords(text)
    text = remove_Ent(text)
    text = get_lem(text)
    text = get_low(text)
    return text
    
