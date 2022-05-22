import requests

from bs4 import BeautifulSoup
word = input()
url_link = input()

r = requests.get(url_link)
soup = BeautifulSoup(r.content, 'html.parser')
paragraphs = soup.find_all('p')
word_list = []
for p in paragraphs:
    if word in p.text:
        print(p.text)
        break