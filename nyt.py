# -*- coding: UTF-8 -*-
import urllib2
import json

for offset in xrange(2):
 print "-"
 base_request = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q='
 apiKey = 'ea4f784109e89c4206e13a5d04dc115a:16:69474324'
 add_query = 'O.J.+Simpson&begin_date=19940101&end_date=19960101&api-key=' + apiKey
 query = base_request + add_query
 response = urllib2.urlopen(query)
 content = response.read()
decoded = json.loads(content)
#print 'CLEANED DATA', json.dumps(decoded, indent=4)

for x in decoded['response']['docs']:
	print x['web_url']
	print x['headline']['main']