import requests

from bs4 import BeautifulSoup
subtitle = int(input())
website = input()

r = requests.get(website)
soup = BeautifulSoup(r.content, 'html.parser')

a = soup.find_all('h2')
heading = a[subtitle]
print(heading.text)