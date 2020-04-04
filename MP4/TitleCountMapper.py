#!/usr/bin/env python3

import sys
import string
import re
import operator


#sys.stdout = open("file.txt", "w+")

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
delimiters = ""

#TODO
with open(stopWordsPath) as f:
    # ,;.?!-:@[](){}_*/
    data = f.read()
    stopwords = re.split("\\n|\\s",data)
    




#TODO 
with open(delimitersPath) as f:
    delimiters=",|;|\.|\?|!|-|:|@|\[|\]|\(|\)|\{|\}|_|\*|\/|\\n| "

for line in sys.stdin:
    # TODO
    words=re.split(delimiters,line.lower());
    for word in words:
        if word not in stopwords and word != '':
            print ("%s\t%s" % (word, 1))
            
            
            
    # print('%s\t%s' % (  ,  )) pass this output to reducer


