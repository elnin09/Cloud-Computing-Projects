#!/usr/bin/env python3
import sys
import re
import operator


# input comes from STDIN
wordcount = dict()

#sys.stdout = open("file3.txt", "w+")
#f = open("file2.txt", "r")

for line in sys.stdin:
    #print(line)
    mapdata = (line.rstrip('\n')).split('\t',2)
    #print(mapdata)
    mapoutputkey,mapoutputcount = mapdata[1],mapdata[2]
    wordcount[mapoutputkey]=int(mapoutputcount)

    # TODO



ret = sorted(wordcount.items(), key=lambda kv: kv[1] )
       
    
size = len(ret)
i=0
ans = list()
while(i<10 and i<size):
    ans.append(ret[size-i-1])
    #print ret[size-i-1]
    i+=1
    
ans.sort(key=lambda x: (x[0],x[1]))
i=0
while(i<10):
    #print(ans[i][0])
    print('%s\t%s' % (ans[i][0],ans[i][1]))
    i+=1   
    # print('%s\t%s' % (  ,  )) print as final output