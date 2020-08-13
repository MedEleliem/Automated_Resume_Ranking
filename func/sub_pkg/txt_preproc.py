
import re
import spacy

def lang_selec(lang):
    if lang == 'fr':
        nlp = spacy.load("fr_core_news_sm")
    elif lang == 'en':
        nlp = spacy.load("en_core_web_sm")
    return nlp

#nlp = lang_selec('fr')
   
def remove_StopWords(text):
    
    sentence = nlp(text)
    filtered_sentence=''
    token_list = []
    for token in sentence : 
        token_list.append(token.text)
    for word in token_list:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop == False :
            filtered_sentence += ' '+word
    filtered_sentence = re.sub('é','e',filtered_sentence)
    filtered_sentence = re.sub('è','e',filtered_sentence)
    filtered_sentence = re.sub('à','a',filtered_sentence)
    filtered_sentence = re.sub('â','a',filtered_sentence)
    return filtered_sentence

def get_lem(text):
    
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text

"""
from nltk.stem.snowball import SnowballStemmer
    def get_stem(text):
    filtered_sentence = ''    
    stemmer = SnowballStemmer(language='french')
    for token in text.split(" "):
        filtered_sentence += ' '+stemmer.stem(token)
    return filtered_sentence 
"""

        
def remove_Ent(text):
    l = ['janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novombre','decembre','mois','an',
         'année','jan','feb','mar','april','june','july','jul','aug','august','september','sep','oct','nov','dec']
    for i in l :
        text = re.sub(i, '', text)
    doc = nlp(text)
    text =''
    ent_type = ['PER','DATE','GPE','LOC']
    for ent in doc:
        if ent.ent_type_ in ent_type:
            text += ''
        else:
            text += ' ' + ent.text
    return text


def get_low(text):
    
    return text.lower()

def remove_SpeChar(text):
    text = re.sub('\W[a-z]\W',' ',text)
    text = re.sub('\W[a-z]\W',' ',text)
    text = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text, flags=re.MULTILINE)
    text = re.sub('\S*@\S*\s?', '', text)
    text = re.sub('\[.*?\]', '', text)
    text = re.sub(r'[^\w]', ' ', text)
    text = re.sub('[!"#$%&()*+,./:;<=>?@[\]^_`{|}~‘’•]', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = " ".join(text.split())
    return text

def main_PreProc(text):
    
    text = remove_StopWords(text)
    text = remove_Ent(text)
    text = get_lem(text)
    text = remove_Ent(text)
    #text = get_stem(text)
    text = get_low(text)
    text = remove_SpeChar(text)
    
    return text