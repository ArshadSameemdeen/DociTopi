import re
import os


def filter_data(filename):
    # remove stopwords
    file1 = open(os.path.join('uploads', filename), encoding='utf-8')
    stopwordfile = open("StopWords.txt", encoding='utf-8')
    readstopword = stopwordfile.read()
    stop_words = readstopword.split()

    line = file1.read()
    words = line.split()

    for r in words:
        if not r in stop_words:
            newFileName = 'filtered_' + filename
            appendFile = open(os.path.join(
                'uploads', newFileName), 'a', encoding='utf-8')
            appendFile.write(''+r)
            appendFile.close()

    return newFileName
