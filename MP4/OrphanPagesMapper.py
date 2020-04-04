#!/usr/bin/env python3
import sys
import re

#sys.stdout = open("fileorphan.txt", "w+")
for line in sys.stdin: 
  key,value = (line.rstrip('\n')).split(':',1);
  values = re.split(" ",value.lstrip(' '));

  #print('%s\t%s\t%s' % (1,key,key))
  for i in values:
    print('%s\t%s\t%s' % (1,i,key.rstrip('\n')))

  # TODO
  
  # print('%s\t%s' % (  ,  )) pass this output to reducer
