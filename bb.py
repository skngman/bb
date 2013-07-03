#!/usr/bin/python
# best bet 

import sys
import os
import pandas as pd
import logparsers

os.linesep = '\n'
#import nltk

if len(sys.argv) < 3:
	print "USAGE:    python ./bb.py logtype inputfilename" 
	print ""
	print "syntax to run program:"
	print "argv(0) is the log type"
	print "argv(1) is the file to analyze"
	sys.exit(0)

if 'libguides' in sys.argv[1]:
	inputpathfile = 'input/' + sys.argv[1] + '/' + sys.argv[2]
	print inputpathfile	
	v = logparsers.geturlsearches(inputpathfile)
	v.sort()
	weillseries = pd.Series(v)
	print weillseries.count()
	outputpathfile = 'output/' + sys.argv[1] + '/' + sys.argv[2] + '-out.csv'
	print outputpathfile
	weillseries.value_counts().to_csv(outputpathfile)


if 'voyager' in sys.argv[1]:
	print 'choice = voyager'
	#import mvoyager
	v = mvoyager.getsearches(sys.argv[2])	
	print len(v)





#	v.sort()
#	for line in v:
#		f.write(line + os.linesep)
#		
#	vunique = list(set(v))
#	vunique.sort()
#	for line in vunique:
#		u.write(line + os.linesep)
#
#	cfilepath = 'output/libguides/libguides-unique-search-terms.tsv'
#	if os.path.exists(cfilepath) is False:
#		print 'gr cluster file is not available'
#	else:
#		print 'gr cluster file is available'
#		cdict = {}
#		with open(cfilepath) as cf:
#			lines = cf.readlines()
#			for i in range (1,len(lines)):
#				cols = lines[i].split("\t")
#				cdict[cols[0]] = cols[1]
#		cleanlist = []
#		for line in v:
#			if line in cdict.keys():
#				cleanlist.append(cdict[line].rstrip())
#		cleanlist.sort()
#		from collections import Counter
#		termcount = Counter()
#		for cleanline in cleanlist:
#			cleaned.write(cleanline + os.linesep)
#			termcount[cleanline] += 1
#		
#		print termcount.most_common(10)
#		cleancount.write('clustered term' + "\t" + 'count' + os.linesep)
#		for key, val in termcount.iteritems():
#			#cleancount.write(key + "\t" + str(val))
#			writeout = key + "\t" + str(val)
#			cleancount.write(writeout + os.linesep)
			
		
		

		

