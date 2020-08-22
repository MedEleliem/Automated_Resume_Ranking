import nlp_resume.text_extract.txt_preproc as txtp
import nlp_resume.word_search.tf_idf_sim as tfidfs
from pymongo import MongoClient

def get_keywords(field, keyword_list, lang, connection_string):
    
    client = MongoClient(connection_string) 
    db = client.NLPIntern
    col = db.Key_words
    l = []
    
    if type(keyword_list) == str and type(field) == str:
        l.append(txtp.main_PreProc((keyword_list, lang)))
        element = {'field':field ,'keyword_list': l}
    
    elif type(keyword_list) == list and type(field) == str:
        for i in keyword_list:
            l.append(txtp.main_PreProc(i, lang))
        element =  {'field':field,'keyword_list':l}
    
    elif type(field) != str:
        raise ('field must be string')
    col.insert_one(element)

def check_sim_keywords(word, connection_string, lang):

    Client = MongoClient(connection_string)
    db = Client.NLPIntern
    
    for j in db.Key_words.find({}):
        keywords = j.get('keyword_list')
        for i in keywords:
            if tfidfs.word_sim(txtp.main_PreProc(i, lang),txtp.main_PreProc(word, lang)) >=75 :
                return keywords
                break      
            else:
                return 'no match found'

        