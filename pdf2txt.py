# -*- coding: utf-8 -*-
import sys
import os
import glob
import keras
import numpy as np
import operator
import csv
import six
import io


from pdfminer3.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfpage import PDFPage
from io import StringIO


#sys.setdefaultencoding('utf-8')


def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)

    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()
    pages = 1
    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        print(pages)
        pages+=1
        interpreter.process_page(page)
    fp.close()
    device.close()
    str = retstr.getvalue()

    texto_procesado = keras.preprocessing.text.text_to_word_sequence(str, filters='\x0c0123456789!"#$%&()*+,-./:;<=>¿?@[\\]^_`{|}~\t\n', lower=True, split=' ')
    #np_texto_procesado = np.array(texto_procesado)

    total_palabras = len(texto_procesado)
    print(path)
    print(total_palabras)

    #lista de palabras a ignorar en el conteo
    blacklist =['o', 'e', 'de', 'que', 'el', 'y', 'a', 'la', 'los', 'un', 'una', 'en', 'las', 'del', 'hay', 'más', 'está', 'estos', 'eso', 'este', 'esta', 'estas', 'para', 'con', 'se', 'como', 'al', 'por', 'as', 'por', 'su', 'sus', 'lo', 'es', 'ha', 'han', 'no', 'nos', 'entre']

    tokenizer = keras.preprocessing.text.Tokenizer(
        num_words=0, 
        filters='01234567890!"#$%&()*+,-./:;<=>¿?@[\\]^_`{|}~\t\n', 
        lower=True, 
        split=' ', 
        char_level=False
    )

    tokenizer.fit_on_texts(texto_procesado)


    for excluida in blacklist:
        if excluida in tokenizer.word_counts:
            print("encontre "+ excluida)
            del tokenizer.word_counts[excluida]

    out = tokenizer.word_counts
    print(out)

    #sorted_out = sorted(out.items(), key=operator.itemgetter(1))

    #print(out)

    retstr.close()
  
    #print sorted_out   
    return out, total_palabras



my_dict, total_palabras = convert_pdf_to_txt("FA.pdf")
with open('FA.csv', 'w') as f:
    for key in my_dict.keys():
        porcentaje = round((my_dict[key]/total_palabras),7)
        if porcentaje >= 0.0001:
            f.write("%s,%s,%s\n"%(key,my_dict[key],porcentaje))
f.close()


my_dict, total_palabras = convert_pdf_to_txt("PN.pdf")
with open('PN.csv', 'w') as f:
    for key in my_dict.keys():
        porcentaje = round((my_dict[key]/total_palabras),7)
        if porcentaje >= 0.0001:
            f.write("%s,%s,%s\n"%(key,my_dict[key],porcentaje))
f.close()

my_dict, total_palabras = convert_pdf_to_txt("PC.pdf")
with open('PC.csv', 'w') as f:
    for key in my_dict.keys():
        porcentaje = round((my_dict[key]/total_palabras),7)
        if porcentaje >= 0.0001:
            f.write("%s,%s,%s\n"%(key,my_dict[key],porcentaje))
f.close()




#convert_pdf_to_txt("PN.pdf")

