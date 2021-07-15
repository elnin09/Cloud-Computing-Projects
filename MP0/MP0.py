import random 
import os
import string
import sys
import re
import operator

stopWordsList = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its",
            "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
            "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having",
            "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
            "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
            "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
            "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
            "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
            "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]


#delimiters = r"[ \t|,|;|.|?|!|-|:|@|[|]|(|)|{|}|_|*|/]"

def getIndexes(seed):
    random.seed(seed)
    n = 10000
    number_of_lines = 50000
    ret = []
    for i in range(0,n):
        ret.append(random.randint(0, 50000-1))
    return ret

def process(userID):
    indexes = getIndexes(userID)
    ret = []

    filename = userID;
    
    #myfile = open('input.txt', 'r')  #read the file 
    lines = list()

    for line in sys.stdin:
        #print line.lower()
        lines.append(line.lower())
        #print(line)
    
    wordcount = dict()
    
    for i in indexes:
        words = re.split(';|,|\*|\\n|\s|\\t|;|\.|\?|!|-|:|@|\[|\]|\(|\)|\{|\}|_|\/',lines[i]);
        #' \t|\,|\;|\.|\?|\!|\-|\:|\@|\[|\]|\(|\)|\{|\}|\_|\*|\/ '
        #words = re.split(' \t|\,|\;|\.|\?|\!|\-|\:|\@|\[|\]|\(|\)|\{|\}|\_|\*|\/ ',lines[i])
        for word in words:
            if word != '' and word not in stopWordsList :
                if word in wordcount:
                    wordcount[word] = wordcount[word]+1
                else:
                    wordcount[word] = 1
    
    #print wordcount
    
    #for k in wordcount:
    #   wordcount[k]=str(wordcount[k])+k

    ret = sorted(wordcount.items(), key=lambda kv: kv[1] )
       
    
    size = len(ret)
    i=0
    ans = list()
    while(i<20 and i<size):
        ans.append(ret[size-i-1])
        #print ret[size-i-1]
        i+=1
    
    ans.sort(key=lambda x: (-x[1], x[0]))
    i=0
    while(i<20):
        print ans[i][0]
        i+=1
    

process(sys.argv[1])

