import urllib.request
import xml.etree.ElementTree as ET
import json


url = input('Enter Desired URL:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2147990.json'

print('Retrieving', url)
data = urllib.request.urlopen(url)
us = data.read().decode()
info = json.loads(us)
print('Retrieved',len(us),'characters')

total = 0
for user in info['comments']:
    total = total + user['count']


print('User count:', total)

