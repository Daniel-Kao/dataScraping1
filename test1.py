from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        title = bsObj.body.h1
    except ArithmeticError as e:
        return None
    return title

title = getTitle('https://bbs.hupu.com/')

if title == None:
    print('nothing here')
else:
    print(title)