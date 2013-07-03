
def geturlsearches(file):
	import urllib
	from urlparse import urlparse
	import re
	allsearches = []
	with open(file) as f:
	  lines = f.readlines()
	
	for i in range (3,len(lines)-1):
		print i
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

	return allsearches
