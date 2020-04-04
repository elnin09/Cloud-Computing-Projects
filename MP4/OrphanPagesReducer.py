#!/usr/bin/env python3
import sys


#TODO
keydata = dict()
#f = open("fileorphan.txt", "r")

for line in sys.stdin:
  mapdata = (line.rstrip('\n')).split('\t',2)
  key,value = int(mapdata[1]),int(mapdata[2])

  if key in keydata.keys():
      keydata[key]=keydata[key]+1
      if value not in keydata.keys():
        keydata[value]=0
  else:
    keydata[key]=1
    if value not in keydata.keys():
      keydata[value]=0

ids = []

for key in keydata.keys():
  if keydata[key] == 0:
    ids.append(str(key))
ids.sort()

for id in ids:
  print(id)

#TODO
# print(xx) print as final output