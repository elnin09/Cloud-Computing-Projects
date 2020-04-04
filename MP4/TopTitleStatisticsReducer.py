#!/usr/bin/env python3
import sys
import math


#TODO
countarray=[]
for line in sys.stdin:
    mapdata = (line.rstrip('\n')).split('\t',2)
    mapoutputkey,mapoutputcount = mapdata[1],mapdata[2]
    countarray.append(int(mapoutputcount))
    
mean = 0
maxn  = 0
minn  = 10000000
sumn  = 0
var = 0
count = 0

for number in countarray:
    sumn = sumn+number;
    count = count+1;
    if number < minn:
        minn = number
    if number > maxn:
        maxn = number
mean = sumn/count    

for number in countarray:
    var = var + pow(abs(mean-number),2)

var = var/count
print('%s\t%s' % ("Mean",int(mean)))
print('%s\t%s' % ("Sum",int(sumn))) 
print('%s\t%s' % ("Min",int(minn))) 
print('%s\t%s' % ("Max",int(maxn))) 
print('%s\t%s' % ("Var",int(var)))  



#TODO
# print('%s\t%s' % (  ,  )) print as final output
