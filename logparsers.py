
def geturlsearches(file):
	import sys
	import urllib
	from urlparse import urlparse
	import re
	allsearches = []
	with open(file) as f:
	  lines = f.readlines()
	
	for i in range (3,len(lines)-1):
		try:
			for tup in range (0, int(lines[i].split()[1])):
				o = urlparse(lines[i].split()[0])
				q = o.query.split('&')
				for val in q:
					if 'q=' in val:
						thesearch = val.split('=')[1]
						if len(thesearch) > 1:
							thesearch = urllib.unquote(thesearch).strip().lower().translate(None, '"')
							thesearch = thesearch.replace('%22', ' ')
							thesearch = thesearch.replace("\t", ' ')
							thesearch = thesearch.replace("+", ' ')
							allsearches.append(thesearch)
		except Exception:
			sys.exc_clear()
	return allsearches


def getvoyagersearches(file):
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
