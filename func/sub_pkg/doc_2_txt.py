from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from docx2pdf import convert
import re
from io import StringIO
import os


def doc2pdf(path):
    
    new_path = re.sub('docx','pdf',path)
    
    convert(path, new_path)
    return new_path
    

def convert_pdf_to_txt(path):
    
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 10
    caching = True
    pagenos=set()
    
    base = os.path.basename(path)
    ext = os.path.splitext(base)[1]
    if ext == '.pdf':
        fp = open(path, 'rb')
        
    elif ext == '.docx':
        path = doc2pdf(path)
        fp = open(path, 'rb')
        
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            interpreter.process_page(page)

    text = retstr.getvalue()
    text = re.sub('\n', ' ', text)
        
    fp.close()
    device.close()
    retstr.close()
    
    return text