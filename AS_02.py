import urllib.request
import xml.etree.ElementTree as ET

url = input('Enter Desired URL:')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_2147989.xml'

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved',len(data),'characters')
tree = ET.fromstring(data)

count = 0
counts = tree.findall('.//count')
nums = list()
for result in counts:
    # Debug print the data :)
    nums.append(int(result.text))
    count = count + 1

print('Count:', count)
print('Sum:', sum(nums))
