#!/usr/bin/python

import urllib
from urlparse import urlparse

def getsearches(file):
	allsearches = []
	with open(file) as f:
	    lines = f.readlines()
	
	for i in range (3,len(lines)-1):
		for tup in range (0, int(lines[i].split()[1])):
			o = urlparse(lines[i].split()[0])
			q = o.query.split('&')
			for val in q:
				if 'Search_Arg' in val:
					thesearch = val.split('=')[1].replace('+', ' ')
					print thesearch
					allsearches.append(urllib.unquote(thesearch).strip())
	
	return allsearches

