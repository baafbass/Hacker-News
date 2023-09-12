import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find_all('div'))
print(soup)
print(soup.find('a')) # return the anchor it found
print('')
print(soup.body)
print(soup.title)