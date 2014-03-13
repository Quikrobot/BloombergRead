from bs4 import BeautifulSoup
import urllib.request
import datetime


url1 = 'http://mobile.bloomberg.com/markets/stocks/world-indexes/europe-africa-middle-east/'
url2 = 'http://mobile.bloomberg.com/markets/stocks/world-indexes/americas/'
url3 = 'http://mobile.bloomberg.com/markets/stocks/world-indexes/asia-pacific/'

values = {'location' : 'US',
          'language' : 'English' }
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1)' }
data  = urllib.parse.urlencode(values)
data = data.encode('utf-8')

def parseIndex(soup):
    for link in soup.find_all('div','data-row'):
#       print('************************')
#        print(link.getText)
#       print('************************')
        index = link.find('a').find(text=True).replace(';','').strip()
        time = link.find('span','time stock-time').find(text=True).replace(';','').strip()
        value = link.find('span','value stock-value').find('span').find('span').find(text=True).replace(',','').strip()
        ls =   datetime.datetime.now().strftime("%Y%m%d %H:%M") + ';' + index + ';' + time + ';' + value + '\n'
        file.write(ls)


fileName = datetime.datetime.now().strftime("%Y%m%d%H%M") + '.txt'
print(fileName)
file = open(fileName, 'w')

req = urllib.request.Request(url1, data, headers)
soup = BeautifulSoup(urllib.request.urlopen(req))
parseIndex(soup)

req = urllib.request.Request(url2, data, headers)
soup = BeautifulSoup(urllib.request.urlopen(req))
parseIndex(soup)

req = urllib.request.Request(url3, data, headers)
soup = BeautifulSoup(urllib.request.urlopen(req))
parseIndex(soup)

file.close()



