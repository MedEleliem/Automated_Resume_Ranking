import os
import re
import uuid
from pre_proc_ import main_

def path_selector(path):
    """ this function will return a list of all files paths with pdf format"""
    L=[]
    for filename in os.listdir(path):
        if filename.endswith('.pdf'):
            L.append({'name': filename, 'path': os.path.join(path, filename)})
    return L



def insert_into(path):
    List = []
    id = uuid.uuid1()
    path_selector(path)
    for i in path_selector(path):
            List.append({'id' : id ,'name' : re.sub('[\d+ .pdf !"#$%&()*+,./:;<=>?@[\]^_`{|}~‘’• CV cv Resume resume ]','',i.get('name')) , 'text' : main_(i.get('path'))})
    return List