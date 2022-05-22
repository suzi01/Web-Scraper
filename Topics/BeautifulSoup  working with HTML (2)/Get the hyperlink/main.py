import requests

from bs4 import BeautifulSoup

page_number = int(input())
url_link = input()

r = requests.get(url_link)
soup = BeautifulSoup(r.content, 'html.parser')

a = soup.find_all('a')
h_link = a[page_number - 1]
print(h_link.get('href'))
