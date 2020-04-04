#!/usr/bin/env python3
import sys
import re

leaguePath = sys.argv[1]
#TODO

with open(leaguePath) as f:
       data = f.read()
       words = re.split("\\n|\\s",data)
	





for line in sys.stdin:
       key,count = line.split('\t', 1)

       if key in words:
              print('%s\t%s\t%s' % (1,key,count.rstrip('\n')))

       #TODO

       # print('%s\t%s' % (  ,  )) pass this output to reducer
