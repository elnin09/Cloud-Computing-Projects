#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext
import re

conf = SparkConf().setMaster("local").setAppName("OrphanPages")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1], 1) 

#TODO

output = open(sys.argv[2], "w")


def mapperfunction(line):
    retval=list()
    key,value = (line.rstrip('\n')).split(':',1);
    values = re.split(" ",value.lstrip(' '));
    for i in values:
        retval.append((i,key.rstrip('\n')))
    return retval
    
def mapfunction(x):
    retval = list()
    retval.append((x[0],1))
    retval.append((x[1],0))

def reducehelper(x):
    if(int(x[1]) == 0):
        return str(x[0])

print("Luada 1")
wcflatmap = lines.flatMap(lambda x:mapperfunction(x))
print(wcflatmap.take(10))
print("Lauda 2")
wc = wcflatmap.flatMap(lambda x: mapfunction(x));
print(wc.take(30))
print("lauda3")
wcreduce = wc.reduceByKey(lambda a, b: a + b)
print(wcreduce.take(30))
print("lauda3")
wcreduce = wcreduce.flatMap(lambda x: reducehelper(x));
print(wcreduce.take(30))


valuesorted = wcreduce.sortBy(lambda a: -a)


for i in valuesorted:
    print(i)

#TODO
#write results to output file. Foramt for each line: (line+"\n")

sc.stop()

