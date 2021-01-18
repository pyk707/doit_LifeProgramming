import os, re
import csv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = 'https://news.daum.net/'
#bs(html.read(), 'html.parser')
soup = bs(ur.urlopen(news).read(), 'html.parser')

soup.find_all('div', {"class" : "relate_thumb"})
for i in soup.find_all('div', {"class" : "relate_thumb"}):
    print(i.text)

for i in soup.find_all('a')[:5]:
    print(i.get('href'))


article1 = 'https://news.v.daum.net/v/20210118214828328'
soup2 = bs(ur.urlopen(article1).read(), 'html.parser')

for i in soup2.find_all('p'):
    print(i.text)
