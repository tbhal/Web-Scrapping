import urllib3
from bs4 import BeautifulSoup

url = 'https://www.bloomberg.com/quote/SPX:IND'

page = urllib3.PoolManager()

response = page.request('GET', url)

soup = BeautifulSoup(response.data)

name_box = soup.find('h1', attrs={'class': 'name'})
name = name_box.text.strip()
print(name)

price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print(price)

