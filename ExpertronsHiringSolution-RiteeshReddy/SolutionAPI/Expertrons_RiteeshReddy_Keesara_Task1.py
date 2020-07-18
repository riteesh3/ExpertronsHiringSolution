import urllib.request, urllib.parse, urllib.error
import json
import ssl

apikey = 'f0d82ca94fba4dc9841ce516fa7506ae'
serviceurl = 'https://newsapi.org/v2/top-headlines?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

query = input("Enter Query : ")
sources = input("Enter Source : ")
op = int(input("choose 1.Query 2.Source : "))

parms = dict()
if op == 1:
	parms['q'] = query
	opt = int(input("Choose by 1.publishedAt 2.default: "))
	if opt == 1:
		date = input("enter date in UTC format: ")
		parms['publishedAt'] = date
	else:
		pass

else:
	parms['sources'] = sources

if apikey is not False: parms['apikey'] = apikey
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
print()
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

try:
   js = json.loads(data)
except:
    js = None

articles = js['articles']
for i in articles:
	print(i['title'])
	print()