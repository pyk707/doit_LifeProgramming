#beautifulsoap4 설치 → HTML과 XML 문서에서 원하는 정보를 쉽게 추출할 수 있는 모듈을 모아둠
#pip install beautifulsoup4

import os, re
import csv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs


#soup = bs(ur.urlopen('http://quotes.toscrape.com/').read(),'html.parser')
url = 'http://quotes.toscrape.com/'
html = ur.urlopen(url)
soup = bs(html.read(), 'html.parser')

#우선 soup를 출력해서 어떤 태그를 가져올 것인지 고민
#그리고 .find_all을 사용
quote = soup.find_all('span')
print(quote[0])
#text값만 추출하기
print()
for i in quote:
    i.text

#class 속성값이 quote인 <div> 태그에 들어 있는 텍스트만 불러오라고 다음과 같이 명령
#이제 class="quote"인 <div> 태그 안에서 텍스트 내용만 추출
for i in soup.find_all('div', {"class" : "quote"}):
    print(i.text)


