import urllib.request, urllib.parse, urllib.error
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
j = urllib.request.urlopen(url, context=ctx)

data = j.read()
print('Retrieved', len(data), 'characters')

info = json.loads(data)
l = info['comments']
print('Count:', len(l))
summ = 0
for i in l:
    nom = int(i["count"])
    summ = summ + nom
print('Sum:', (summ))
