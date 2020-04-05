#!/usr/bin/env python

'''Exectuion Command: spark-submit TitleCountSpark.py stopwords.txt delimiters.txt dataset/titles/ dataset/output'''

import sys
from pyspark import SparkConf, SparkContext
import re

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]
delimiters = ""

with open(stopWordsPath) as f:
    data = f.read()
    stopwords = re.split("\\n|\\s",data)
	#TODO

with open(delimitersPath) as f:
    delimiters=",|;|\.|\?|!|-|:|@|\[|\]|\(|\)|\{|\}|_|\*|\/|\\n| "
    #TODO

conf = SparkConf().setMaster("local").setAppName("TitleCount")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[3],1)

outputFile = open(sys.argv[4],"w")
sys.stdout = outputFile
#print("lauda")

def titlecountmap(line):
    retval = list()
    words=re.split(delimiters,line.lower());
    for word in words:
        if word not in stopwords and word != '':
            retval.append(word)
    return retval
    

wcflatmap = lines.flatMap(lambda x:titlecountmap(x))


wc = wcflatmap.map(lambda x: (x,1))
#print("lauda")
#print(wc.take(30))
#print("lauda")
wcreduce = wc.reduceByKey(lambda a, b: a + b)

valuesorted = wcreduce.sortBy(lambda a: -a[1])
valuefinesorted = wcreduce.sortBy(lambda a: a[0])


finallist = valuesorted.take(10)
for i in finallist:
    print('%s\t%s' % (i[0], i[1]) )
#TODO



#print(wcreduce.collect())


#TODO
#write results to output file. Foramt for each line: (line +"\n")

sc.stop()
