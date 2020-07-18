import urllib.request, urllib.parse, urllib.error
import json
import ssl

apikey = 'f7KANRgLxDMTLMgK3JmEMDfHUquVHSbK'
serviceurl = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
parms = dict()

query = 'Indigo'
parms['q'] = query

if apikey is not False: parms['api-key'] = apikey
url = serviceurl + urllib.parse.urlencode(parms)
print('Retrieving', url)
print()
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()

try:
   js = json.loads(data)
except:
    js = None

for i in range(10):
	out = js['response']['docs'][i]['web_url']
	print(out)