from pymongo import MongoClient

from get_text_info import insert_text_into

def mongo_db_insert_raw_text(connection_string, path):

    client = MongoClient(connection_string) 
    db = client.NLPIntern
    col = db.Resume
    
    to_insert = insert_text_into(path) 
    
    if type(to_insert) == dict : 
        col.insert_one(to_insert)

    elif type(to_insert) == list : 
        col.insert_many(to_insert)