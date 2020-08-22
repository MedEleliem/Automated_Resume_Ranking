import nlp_resume.text_insert.db_insert as txti
import nlp_resume.keyword_insert.get_keywords as ki
import nlp_resume.word_search.tf_idf_sim as ws
import nlp_resume.text_extract.txt_preproc as te
from pymongo import MongoClient

if __name__ == '__main__':
    print("This is an automated ranking resume application \n")
    language = input('enter en or fr for the langauge treatement \n').lower()
    connection_string = input('enter the connection string to MongoDB \n').lower()

    while True:
        action = input("What should I do? [I]mport_files, [A]dd_Keywords, [S]earch_for_words, or [Q]uit ? \n").upper()

        if action == 'I':
            path = input('enter the path to resume files \n')
            txti.mongo_db_insert(connection_string, path, language)

        if action == 'A':
            keywords_dict = []
            keywords_field = input('enter the field of keywords \n')
            keywords_list = input("enter the list of keywords splitted by white-space \n")
            keywords_list = keywords_list.split(' ')
            ki.get_keywords(keywords_field, keywords_list, language, connection_string)

        if action == 'S':
            word = input('enter the sentence to search \n')
            word = te.main_PreProc(word,language)
            Client = MongoClient(connection_string)
            db = Client.NLPIntern
            n = db.Key_words.count_documents({})
            m = db.Resume.count_documents({})
            check = ki.check_sim_keywords(word, connection_string, language)

            if check != 'no match found':

                if n == 0 and m != 0:
                    print(ws.tf_idf_(word, connection_string))
                elif n != 0 and m != 0:
                    if len(check) != 0:
                        for i in check:
                            print(ws.tf_idf_(i, connection_string))
                    else:
                        print(ws.tf_idf_(word, connection_string))
            else:
                print(ws.tf_idf_(word, connection_string))

        if action == 'Q':
            raise SystemExit()
