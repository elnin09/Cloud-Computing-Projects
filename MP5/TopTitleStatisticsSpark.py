#!/usr/bin/env python
import sys
from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("TopTitleStatistics")
conf.set("spark.driver.bindAddress", "127.0.0.1")
sc = SparkContext(conf = conf)

lines = sc.textFile(sys.argv[1],1)

#TODO

def mymap(x):
    mapoutputkey,mapoutputcount = x.split('\t', 1)
    return int(mapoutputcount)

wc = lines.map(mymap)

outputFile = open(sys.argv[2],"w")

#TODO write your output here
#write results to output file. Format
ans1 = int(wc.sum()/wc.count())
outputFile.write('Mean\t%s\n' % ans1)
ans2 = wc.sum()
outputFile.write('Sum\t%s\n' % ans2)
ans3 = wc.min()
outputFile.write('Min\t%s\n' % ans3)
ans4 = wc.max()
outputFile.write('Max\t%s\n' % ans4)
ans5 = int(wc.variance())
outputFile.write('Var\t%s\n' % ans5)


sc.stop()

