#!/usr/bin/python
# best bet 

import sys
#import nltk

if 'voyager' in sys.argv[1]:
	print 'choice = voyager'
	import mvoyager
	v = mvoyager.getsearches(sys.argv[2])	
	print len(v)

if 'libguides' in sys.argv[1]:
	print 'choice = libguides'
	import mlibguides
	v = mlibguides.getsearches(sys.argv[2])	
	print len(v)
	#for line in v:
		#print line
