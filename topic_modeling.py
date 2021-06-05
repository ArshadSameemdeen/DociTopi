from gensim import corpora, models
import gensim
import os
from os import path
from time import sleep
import time
import shutil


def modeled_topic(file):

    #filename_2 = file
    file1 = open(os.path.join('uploads', file), encoding='utf-8')
    filee = file1.read()
    print(file)

    tdm = []

    # insert stopwords files
    stopwordfile = open("StopWords.txt", encoding='utf-8')

    # split the words
    words = filee.split()

    readstopword = stopwordfile.read()
    stop_words = readstopword.split()

    for r in words:
        if not r in stop_words:
            tdm.append(r)
    tdm = [tdm]

    dictionary = corpora.Dictionary(tdm)
    corpus = [dictionary.doc2bow(i) for i in tdm]
    sleep(3)

    # Implemented the LdaModel
    ldamodel = gensim.models.ldamodel.LdaModel(
        corpus, num_topics=10, id2word=dictionary)

    my_dict = {'Topic_' + str(i): [token for token, score in ldamodel.show_topic(
        i, topn=1)] for i in range(0, ldamodel.num_topics)}

    topic_list = my_dict['Topic_0']
    final_topic = topic_list[0]

    dstDir = "New data\\modeled_topics"
    move_file = os.path.join('uploads', file)
    file1.close()
    shutil.move(move_file, dstDir)

    return final_topic
