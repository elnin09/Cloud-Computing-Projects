#!/usr/bin/env python3
import sys





for line in sys.stdin:
       mapoutputkey,mapoutputcount = line.split('\t', 1)
       print('%s\t%s' % (1,line.rstrip('\n')) )