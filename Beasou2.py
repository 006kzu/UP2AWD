# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Crombie.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")


count = 0
while count <= 6:
    samples = []
    tags = soup('a')
    for tag in tags:
        samples.append(tag.get('href', None))
    newurl = samples[17]
    name1 = re.findall('by_(.+).html', newurl)
    name = name1[0]
    print(name)
    html = urlopen(newurl, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    count = count + 1





