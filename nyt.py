# -*- coding: UTF-8 -*-
import urllib2
import json
def year(d):
 return d[0:4] 

def month(d):
 return d[4:6]

def day(d):
 return d[6:8]
f = open('newfile','w')
for offset in xrange(2):
 print "-"
 base_request = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?q='
 apiKey = 'ea4f784109e89c4206e13a5d04dc115a:16:69474324'
 add_query = 'O.J.+Simpson&begin_date=19940101&end_date=19960101&api-key=' + apiKey
 query = base_request + add_query
 response = urllib2.urlopen(query)
 content = response.read()
 #decoded = json.loads(response_string)
decoded = json.loads(content)
print decoded
#for x in decoded['results']:
 #string = x['date']
 #print(year(string) + " " + month(string) + " " + day(string)+"\t")
# print((x['title'].encode('utf-8') ).replace("’","'").replace("'","'")+"\t")
# print(x['url']+"\n")
#raw_input("Press enter to quit")