from math import log
from fuzzywuzzy import fuzz


from pymongo import MongoClient
Client = MongoClient("mongodb+srv://misooo123:miso1212@nlpintern.9ghch.mongodb.net/Resume?retryWrites=true&w=majority")
db = Client.NLPIntern
d = db.Resume

def word_sim(a,b):
    l =[fuzz.ratio(a,b),fuzz.partial_ratio(a,b),fuzz.token_sort_ratio(a,b),fuzz.token_set_ratio(a,b)]
    if len(a)==len(b):
        l.remove(fuzz.partial_ratio(a,b)) 
        return max(l)
    else:
        return max(l)

def tf_idf_(word,d):
    n=0
    counter=[]
    tot_docs = d.count_documents({})
    tf_idf_list=[]
    freq_list=[]
    for i in range(tot_docs):
        tokens = d.find({})[i].get('tokens')
        name=d.find({})[i].get('name')
        c=0
        n=0
        for j in tokens:
            score = word_sim(word,j)
            if score > 80 :
                c=1
                n+=1
        counter.append(c)
        freq_list.append((n/len(tokens),name))
    app_word_tot = sum(counter)    
    if app_word_tot!=0:
        idf = log(tot_docs/app_word_tot)
        for i in freq_list:
            tf_idf_list.append((i[0]*idf,i[1]))
        return tf_idf_list
    else:
        return 'no match'