from pymongo import MongoClient
import nlp_resume.text_insert.get_text_info as gti

def mongo_db_insert(connection_string, path, lang):

    client = MongoClient(connection_string) 
    db = client.NLPIntern
    col = db.Resume
    
    to_insert = gti.insert_text_into(path, lang)
    
    if type(to_insert) == dict : 
        col.insert_one(to_insert)

    elif type(to_insert) == list : 
        col.insert_many(to_insert)