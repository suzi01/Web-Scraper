import requests
import string
import os

from bs4 import BeautifulSoup

numberOfPages = int(input('Number of pages.'))
typeOfArticle = input('type of article')


for i in range(1, numberOfPages+1):
    #saved_articles = []
    parent_directory = 'C:\\Users\\suzan\\Web Scraper\\Web Scraper\\task'
    print(parent_directory)
    directory_name = 'Page_' + str(i)
    path = os.path.join(parent_directory, directory_name)
    os.mkdir(path)
    os.chdir(path)
    print(os.getcwd())

    user_url = 'https://www.nature.com/nature/articles'
    r = requests.get(user_url +'?searchType=journalSearch&sort=PubDate&page='+str(i), headers={'Accept-Language':'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')

    try1 = soup.find_all('li', class_="app-article-list-row__item")
    for article in try1:
        type = article.find('span', class_="c-meta__type")
        if type.text == typeOfArticle:
            #print('type.test', type.text)
            link = article.a.get('href')
            web_url = "https://www.nature.com" + link
            req = requests.get(web_url)
            soup1 = BeautifulSoup(req.content, 'html.parser')
            try:
                paragraph_1 = soup1.find("div", class_="c-article-body u-clearfix").get_text().strip()
            except AttributeError:
                try:
                    paragraph_1 = soup1.find("div", class_="article-item__body").get_text().strip()
                except AttributeError:
                    print('Unable to proceed')
            paragraph_1 = paragraph_1.replace('\n','')

            title = article.a.text.strip()
            #print('title',title)
            result = list(string.punctuation)

            for p in title:
                if p in result:
                    title = title.replace(p,"")

            title1 = title.replace(' ','_')
            #print('title1',title1)


            file = open(f'{title1}.txt', 'wb')
            file.write(paragraph_1.encode())
            file.close()
            #saved_articles.append(title1)

#print('Saved Articles :', saved_articles)


