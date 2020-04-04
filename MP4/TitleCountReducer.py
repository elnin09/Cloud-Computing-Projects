#!/usr/bin/env python3
from operator import itemgetter
import sys
import re

#TODO

wordcount = dict()



# input comes from STDIN
for line in sys.stdin:
    word, count = line.split('\t', 1)
    if word in wordcount.keys():
        wordcount[word] = wordcount[word] +1
    else:
        wordcount[word] = 1


# TODO
for  k in wordcount.keys():
    print ('%s\t%s' % (str(k), str(wordcount[k])))

# print('%s\t%s' % (  ,  )) print as final output