#!/usr/bin/env python3
import sys

#TODO

keydata = dict()
# input comes from STDIN
for line in sys.stdin:
    mapdata = (line.rstrip('\n')).split('\t',1)
    key,value = int(mapdata[0]),int(mapdata[1])

    if key in keydata.keys():
        keydata[key]=keydata[key]+1
        #if value not in keydata.keys():
            #keydata[value]=0
    else:
        keydata[key]=1
        #if value not in keydata.keys():
            #keydata[value]=0   

for key in keydata.keys():
    print('%s\t%s' % (key,keydata[key]))

# TODO
# print('%s\t%s' % (  ,  )) print as final output