#!/usr/bin/python

import sys
import nltk

if 'voyager' in sys.argv[1]:
	print 'choice = voyager'
	import mvoyager
	v = mvoyager.getsearches(sys.argv[2])	
	print len(v)


